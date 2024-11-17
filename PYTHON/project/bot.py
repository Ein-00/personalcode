import os
import numpy as np
import librosa
import soundfile as sf
import noisereduce as nr
import telebot
from pymongo import MongoClient
from sklearn.metrics.pairwise import cosine_similarity
from connect import getdb
import speech_recognition as sr
from fuzzywuzzy import fuzz

# Replace with your actual Telegram Bot Token
BOT_TOKEN = '7812527416:AAHVU5DOCX2k_QQr-upg4QpsrGH0sqiCB-M'

class VoicePreprocessor:
    @staticmethod
    def preprocess_audio(input_file, output_file=None):
        """
        Comprehensive audio preprocessing method

        Steps:
        1. Load audio file
        2. Reduce noise
        3. Normalize amplitude
        4. Trim silence
        5. Resample to standard rate
        """
        try:
            # Read the audio file
            audio, sample_rate = sf.read(input_file)

            # Convert to mono if stereo
            if len(audio.shape) > 1:
                audio = audio.mean(axis=1)

            # Noise reduction
            reduced_noise = nr.reduce_noise(
                y=audio,
                sr=sample_rate,
                prop_decrease=0.8,  # Aggressive noise reduction
                n_std_thresh_stationary=1.5,
                stationary=True
            )

            # Normalize amplitude
            normalized_audio = librosa.util.normalize(reduced_noise)

            # Trim silence from beginning and end
            trimmed_audio, _ = librosa.effects.trim(
                normalized_audio,
                top_db=30  # Adjust this value to control silence threshold
            )

            # Resample to standard rate (16kHz is good for voice)
            target_sr = 16000
            resampled_audio = librosa.resample(
                trimmed_audio,
                orig_sr=sample_rate,
                target_sr=target_sr
            )

            # Optional: save preprocessed file
            if output_file:
                sf.write(output_file, resampled_audio, target_sr)

            return resampled_audio, target_sr

        except Exception as e:
            print(f"Audio preprocessing error: {e}")
            return None, None


class VoiceAuthenticator:
    def _init_(self, mongo_uri='mongodb://localhost:27017/',
                 database='voice',
                 collection='users'):
        """
        Initialize MongoDB connection and voice authenticator
        """
        self.db = getdb()
        self.collection = self.db["voice"]
        x = self.db["userdata"]
        self.passphrase_collection = x["phrases"]
        self.dbphrase = self.db['phrases']

        # Similarity threshold (adjust based on your testing)
        self.SIMILARITY_THRESHOLD = 0.98
        self.VOICE_RECORDINGS_DIR = 'user_voices_processed'

        # Create directory if it doesn't exist
        os.makedirs(self.VOICE_RECORDINGS_DIR, exist_ok=True)

    def extract_mfcc(self, file_path):
        """
        Extract MFCC features from preprocessed audio file
        """
        try:
            # Use preprocessor to clean audio first
            preprocessed_audio, sr = VoicePreprocessor.preprocess_audio(file_path)

            if preprocessed_audio is None:
                return None

            # Extract more robust MFCC features
            mfccs = librosa.feature.mfcc(
                y=preprocessed_audio,
                sr=sr,
                n_mfcc=20,  # Increased number of coefficients
                n_fft=2048,  # Larger FFT window
                hop_length=512  # Hop length for more detail
            )

            # Compute delta and delta-delta features for more robust representation
            delta_mfccs = librosa.feature.delta(mfccs)
            delta_delta_mfccs = librosa.feature.delta(mfccs, order=2)

            # Combine static, delta, and delta-delta features
            combined_features = np.concatenate([
                np.mean(mfccs, axis=1),
                np.mean(delta_mfccs, axis=1),
                np.mean(delta_delta_mfccs, axis=1)
            ])

            return combined_features.tolist()

        except Exception as e:
            print(f"MFCC extraction error: {e}")
            return None

    def register_user(self, username, voice_file_path):
        """
        Register a new user with noise-reduced voice feature
        """
        # Preprocess and generate a new cleaned file
        processed_file_path = os.path.join(
            self.VOICE_RECORDINGS_DIR,
            f"{username}_processed.wav"
        )

        # Preprocess the audio
        VoicePreprocessor.preprocess_audio(
            voice_file_path,
            processed_file_path
        )

        # Extract features from processed file
        voice_embeddings = self.extract_mfcc(processed_file_path)

        if voice_embeddings is not None:
            user_data = {
                'username': username,
                'voice_embeddings': voice_embeddings
            }

            # Upsert user (insert or update)
            self.collection.update_one(
                {'username': username},
                {'$set': user_data},
                upsert=True
            )
            print(f"Registered/Updated user {username}")
            return True
        else:
            print("Failed to extract voice features")
            return False

    def transcribe_audio(self, audio_path):
        """
        Convert audio to text using SpeechRecognition library
        """
        recognizer = sr.Recognizer()
        try:
            with sr.AudioFile(audio_path) as source:
                audio = recognizer.record(source)
                text = recognizer.recognize_google(audio)
                print(text)
                return text
        except sr.UnknownValueError:
            print("Speech recognition could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        return None

    def get_last_passphrase(self, username):
        """
        Retrieve the last added passphrase for the user
        """
        latest_phrase = self.dbphrase.find_one(sort=[('_id', -1)])
        print(latest_phrase['phrase'])
        return latest_phrase['phrase']

    def authenticate_user(self, username, voice_file_path):
        """
        Authenticate user based on both voice and passphrase match
        """
        processed_file_path = os.path.join(
            self.VOICE_RECORDINGS_DIR,
            f"{username}_auth_processed.wav"
        )

        # Preprocess the audio
        VoicePreprocessor.preprocess_audio(voice_file_path, processed_file_path)

        # Extract features from processed file for voice match
        input_mfcc = self.extract_mfcc(processed_file_path)
        if input_mfcc is None:
            return False

        # Retrieve user data from the database
        user = self.collection.find_one({'username': username})
        if not user:
            return False

        # Convert embeddings to numpy arrays and compute cosine similarity
        input_mfcc_np = np.array(input_mfcc).reshape(1, -1)
        stored_mfcc_np = np.array(user['voice_embeddings']).reshape(1, -1)
        sim_score = cosine_similarity(input_mfcc_np, stored_mfcc_np)[0][0]

        # Retrieve and compare passphrase transcription
        transcribed_text = self.transcribe_audio(processed_file_path)
        stored_passphrase = self.get_last_passphrase(username)

        if not transcribed_text or not stored_passphrase:
            print("lllllllllllllll")
            return False

        # Fuzzy match on passphrase transcription
        passphrase_match_score = fuzz.ratio(transcribed_text, stored_passphrase)

        # Print similarity scores for debugging
        print(f"Voice similarity score: {sim_score}")
        print(f"Passphrase match score: {passphrase_match_score}")
        print(f"Transcription: {transcribed_text}")
        print(f"Stored Passphrase: {stored_passphrase}")

        # Both voice match and passphrase match are required for successful authentication
        return sim_score >= self.SIMILARITY_THRESHOLD and passphrase_match_score >= 80  # Adjust score threshold as needed

# Telegram Bot Setup (similar to previous version)
bot = telebot.TeleBot(BOT_TOKEN)
authenticator = VoiceAuthenticator()


# ... [Rest of the Telegram bot code remains the same as in the previous script]

# Add this function for more detailed logging
def log_authentication(username, success):
    """
    Log authentication attempts
    """
    log_entry = {
        'username': username,
        'success': success
    }
    # You could add MongoDB logging or file-based logging here
    print(f"Authentication for {username}: {'Successful' if success else 'Failed'}")


user_state = {}


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    """
    Welcome message and instructions
    """
    bot.reply_to(message,
                 "Welcome! Voice Authentication Bot\n"
                 "/register - Register a new user\n"
                 "/authenticate - Authenticate an existing user"
                 )


@bot.message_handler(commands=['register'])
def start_registration(message):
    """
    Start user registration process
    """
    bot.reply_to(message, "Please enter your username for registration")
    user_state[message.chat.id] = {'stage': 'username', 'action': 'register'}


@bot.message_handler(commands=['authenticate'])
def start_authentication(message):
    """
    Start authentication process
    """
    bot.reply_to(message, "Please enter your username for authentication")
    user_state[message.chat.id] = {'stage': 'username', 'action': 'authenticate'}


@bot.message_handler(content_types=['text'])
def handle_text(message):
    """
    Handle text messages during registration/authentication
    """
    chat_id = message.chat.id

    if chat_id not in user_state:
        return

    state = user_state[chat_id]

    if state['stage'] == 'username':
        state['username'] = message.text
        bot.reply_to(message, "Now, please send a voice recording")
        state['stage'] = 'voice_record'


@bot.message_handler(content_types=['voice'])
def handle_voice(message):
    chat_id = message.chat.id

    if chat_id not in user_state:
        return

    state = user_state[chat_id]

    try:
        # Download voice file
        file_info = bot.get_file(message.voice.file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        # Create unique filename
        file_path = os.path.join(authenticator.VOICE_RECORDINGS_DIR,
                                 f"{state['username']}_{message.voice.file_id}.wav")

        # Save the file
        with open(file_path, 'wb') as new_file:
            new_file.write(downloaded_file)

        # Perform action based on current state
        if state['action'] == 'register':
            # Registration logic
            success = authenticator.register_user(state['username'], file_path)
            bot.reply_to(message, f"Registration {'successful' if success else 'failed'} for {state['username']}")

        elif state['action'] == 'authenticate':
            # Authentication logic
            auth_result = authenticator.authenticate_user(state['username'], file_path)

            # Log the authentication attempt
            log_authentication(state['username'], auth_result)

            if auth_result:
                bot.reply_to(message, f"✅ Authentication successful for {state['username']}!")
            else:
                bot.reply_to(message, f"❌ Authentication failed for {state['username']}. "
                                      "Voice or passphrase does not match.")

        # Clear the state
        del user_state[chat_id]

    except Exception as e:
        bot.reply_to(message, f"An error occurred: {e}")
        del user_state[chat_id]


# Start the bot
print("Bot is running...")
bot.polling(none_stop=True)

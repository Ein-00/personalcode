
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC
from PIL import Image
import io

# Function to extract and display the image
def extract_image_from_audio(audio_file):
    # Load the audio file
    audio = MP3(audio_file, ID3=ID3)

    # Check for attached images
    for tag in audio.tags.values():
        if isinstance(tag, APIC):
            # Extract the image data
            image_data = tag.data
            
            # Open the image using Pillow
            image = Image.open(io.BytesIO(image_data))
            image.show()
            return

    print("No image found in the audio file.")

# Replace 'path_to_your_audio.mp3' with the path to your audio file
extract_image_from_audio('C:\\Users\\Dell\\Music\Gundam\Akatsuki no Kuruma.mp3')

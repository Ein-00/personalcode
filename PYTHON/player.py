
import pygame
import tkinter as tk
from tkinter import filedialog

def play_audio(file_path):
    # Initialize the mixer module for audio
    pygame.mixer.init()

    # Load the selected audio file
    pygame.mixer.music.load(file_path)

    # Play the audio file
    pygame.mixer.music.play()

    # Wait for the audio file to finish playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

def main():
    # Create a Tkinter root window
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Open a file dialog to choose an audio file
    file_path = filedialog.askopenfilename(
        title="Select an Audio File",
        filetypes=[("Audio Files", "*.mp3 *.wav *.ogg")]
    )

    # If a file is selected, play the audio
    if file_path:
        print(file_path)
        play_audio(file_path)
    else:
        print("No file selected")

if __name__ == "__main__":
    main()

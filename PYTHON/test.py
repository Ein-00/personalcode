
import tkinter as tk
from tkinter import filedialog
import pygame

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Music Player")
        self.root.geometry("300x150")

        # Initialize Pygame mixer
        pygame.mixer.init()

        # Create UI elements
        self.label = tk.Label(root, text="Select a music file")
        self.label.pack(pady=10)

        self.play_button = tk.Button(root, text="Play", command=self.play_music)
        self.play_button.pack(pady=5)

        self.stop_button = tk.Button(root, text="Stop", command=self.stop_music)
        self.stop_button.pack(pady=5)

        self.select_button = tk.Button(root, text="Select File", command=self.select_file)
        self.select_button.pack(pady=5)

        self.file_path = ""

    def select_file(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3 *.wav")])
        if self.file_path:
            self.label.config(text=f"Selected: {self.file_path}")

    def play_music(self):
        if self.file_path:
            pygame.mixer.music.load(self.file_path)
            pygame.mixer.music.play()
        else:
            self.label.config(text="No file selected!")

    def stop_music(self):
        pygame.mixer.music.stop()

if __name__ == "__main__":
    root = tk.Tk()
    player = MusicPlayer(root)
    root.mainloop()

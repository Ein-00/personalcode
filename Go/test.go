
package main

import (
	"fmt"
	"io"
	"os"

	"oto"
	"go-mp3"
)

func main() {
	// Open the MP3 file
	file, err := os.Open("audio.mp3")
	if err != nil {
		fmt.Println("Error opening file:", err)
		return
	}
	defer file.Close()

	// Decode the MP3 file
	decoder, err := mp3.NewDecoder(file)
	if err != nil {
		fmt.Println("Error decoding MP3:", err)
		return
	}

	// Initialize Oto for audio playback
	context, err := oto.NewContext(decoder.SampleRate(), 2, 2, 8192)
	if err != nil {
		fmt.Println("Error initializing Oto:", err)
		return
	}
	defer context.Close()

	player := context.NewPlayer()
	defer player.Close()

	// Play the audio
	if _, err := io.Copy(player, decoder); err != nil {
		fmt.Println("Error playing audio:", err)
		return
	}
}

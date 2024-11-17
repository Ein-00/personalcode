
use rodio::{Decoder, OutputStream, source::Source};
use std::fs::File;
use std::io::BufReader;
use rfd::FileDialog;
use std::time::Duration;

fn main() {
    // Open a file dialog to choose an audio file
    let file_path = FileDialog::new()
        .add_filter("Audio", &["mp3", "wav", "ogg"])
        .pick_file();

    match file_path {
        Some(path) => {
            println!("Selected file: {:?}", path);

            // Try to open the selected file
            let file = File::open(&path).expect("Failed to open file");
            let  decoder = Decoder::new(BufReader::new(file)).expect("Failed to decode audio file");

            // Get the total duration before moving `decoder`
            let duration = decoder.total_duration().unwrap_or(Duration::from_secs(0));

            // Get the default output stream
            let (_stream, stream_handle) = OutputStream::try_default().expect("Failed to get default output stream");

            // Convert samples and play the audio
            let source = decoder.convert_samples();
            let _ = stream_handle.play_raw(source);

            // Wait for the audio to finish playing
            std::thread::sleep(duration);
        }
        None => {
            println!("No file selected");
        }
    }
}


use id3::{Tag, TagLike};
use std::fs::File;
use image::load_from_memory;

fn main() {
    // Replace with the path to your audio file
    let audio_file_path = "C:\\Users\\Dell\\Music\\Gundam\\Ai Senshi.mp3";
    
    // Open the audio file
    let file = File::open(audio_file_path).expect("Failed to open audio file");
    let tag = Tag::read_from(&file).expect("Failed to read ID3 tag");

    // Check for attached pictures
    if let Some(pictures) = tag.clone().pictures().next() {
        // Extract the image data
        let image_data = pictures.data.clone();

        // Load the image from memory
        let img = load_from_memory(&image_data).expect("Failed to load image from memory");

        // Display the image (this will depend on your environment)
        img.save("extracted_image.png").expect("Failed to save image");
        println!("Image extracted and saved as 'extracted_image.png'");
    } else {
        println!("No image found in the audio file.");
    }
}

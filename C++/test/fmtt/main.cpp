#include <iostream>
#include <cryptopp/aes.h>
#include <cryptopp/modes.h>
#include <cryptopp/filters.h>
#include <cryptopp/hex.h>
#include <cryptopp/files.h>
int main() {
    using namespace CryptoPP;

    // Key and IV for AES
    byte key[AES::DEFAULT_KEYLENGTH], iv[AES::BLOCKSIZE];
    memset(key, 0x00, AES::DEFAULT_KEYLENGTH);
    memset(iv, 0x00, AES::BLOCKSIZE);

    // Plaintext to encrypt
    std::string plaintext = "Hello, Crypto++!";
    std::string ciphertext, decryptedtext;

    // Encrypt the plaintext
    try {
        CBC_Mode<AES>::Encryption encryption;
        encryption.SetKeyWithIV(key, sizeof(key), iv);

        StringSource encryptor(plaintext, true,
            new StreamTransformationFilter(encryption,
                new StringSink(ciphertext)
            )
        );
    } catch (const Exception& e) {
        std::cerr << "Encryption error: " << e.what() << std::endl;
        return 1;
    }

    // Decrypt the ciphertext
    try {
        CBC_Mode<AES>::Decryption decryption;
        decryption.SetKeyWithIV(key, sizeof(key), iv);

        StringSource decryptor(ciphertext, true,
            new StreamTransformationFilter(decryption,
                new StringSink(decryptedtext)
            )
        );
    } catch (const Exception& e) {
        std::cerr << "Decryption error: " << e.what() << std::endl;
        return 1;
    }

    // Output results
    std::cout << "Plaintext: " << plaintext << std::endl;
    std::cout << "Ciphertext (hex): ";
    
    // Convert ciphertext to hex format for readability
    StringSource hexEncoder(ciphertext, true, 
        new HexEncoder(new FileSink(std::cout))
    );
    std::cout << std::endl;

    std::cout << "Decrypted text: " << decryptedtext << std::endl;

    return 0;
}

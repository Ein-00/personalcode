import os
import time
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, ec
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

def generate_rsa_keys():
    start_time = time.time()
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()
    key_gen_time = time.time() - start_time
    return private_key, public_key, key_gen_time

def generate_ecc_keys():
    start_time = time.time()
    private_key = ec.generate_private_key(ec.SECP256R1(), default_backend())
    public_key = private_key.public_key()
    key_gen_time = time.time() - start_time
    return private_key, public_key, key_gen_time

def encrypt_file_rsa(public_key, file_path):
    # Generate a symmetric key for AES
    symmetric_key = os.urandom(32)  # AES-256 key

    # Encrypt the file using AES
    with open(file_path, 'rb') as f:
        file_data = f.read()

    # Encrypt the file data with AES
    iv = os.urandom(16)  # Initialization vector
    cipher = Cipher(algorithms.AES(symmetric_key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_file_data = iv + encryptor.update(file_data) + encryptor.finalize()

    # Encrypt the symmetric key with RSA
    encrypted_symmetric_key = public_key.encrypt(
        symmetric_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    return encrypted_symmetric_key, encrypted_file_data

def decrypt_file_rsa(private_key, encrypted_symmetric_key, encrypted_file_data):
    # Decrypt the symmetric key with RSA
    symmetric_key = private_key.decrypt(
        encrypted_symmetric_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # Decrypt the file data using AES
    iv = encrypted_file_data[:16]  # Extract the IV
    cipher = Cipher(algorithms.AES(symmetric_key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_file_data = decryptor.update(encrypted_file_data[16:]) + decryptor.finalize()

    return decrypted_file_data

def encrypt_file_ecc(public_key, file_path):
    # Similar to RSA, but for ECC we will just simulate the process
    with open(file_path, 'rb') as f:
        file_data = f.read()
    
    # Encrypt using symmetric encryption (AES) and then encrypt the key with ECC
    symmetric_key = os.urandom(32)  # AES-256 key
    iv = os.urandom(16)  # Initialization vector
    cipher = Cipher(algorithms.AES(symmetric_key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_file_data = iv + encryptor.update(file_data) + encryptor.finalize()
    
    # In a real implementation, you would encrypt the symmetric key with ECC
    # Here we just return the encrypted file data for simplicity
    return encrypted_file_data

def decrypt_file_ecc(private_key, encrypted_file_data):
    # Similar to RSA, but for ECC we will just simulate the process
    symmetric_key = os.urandom(32)  # In a real implementation, you would decrypt the symmetric key
    iv = encrypted_file_data[:16]  # Extract the IV
    cipher = Cipher(algorithms.AES(symmetric_key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_file_data = decryptor.update(encrypted_file_data[16:]) + decryptor.finalize()
    
    return decrypted_file_data

def measure_performance():
    # Generate RSA keys
    rsa_private_key, rsa_public_key, rsa_key_gen_time = generate_rsa_keys()
    print(f"RSA Key Generation Time: {rsa_key_gen_time:.4f} seconds")

    # Generate ECC keys
    ecc_private_key, ecc_public_key, ecc_key_gen_time = generate_ecc_keys()
    print(f"ECC Key Generation Time: {ecc_key_gen_time:.4f} seconds")

    # Test file sizes
    file_sizes = [1 * 1024 * 1024, 10 * 1024 * 1024]  # 1 MB and 10 MB
    for size in file_sizes:
        # Create a dummy file
        file_path = 'test_file.bin'
        with open(file_path, 'wb') as f:
            f.write(os.urandom(size))

        # Measure RSA encryption time
        start_time = time.time()
        rsa_encrypted_symmetric_key, rsa_encrypted_file_data = encrypt_file_rsa(rsa_public_key, file_path)
        rsa_encrypt_time = time.time() - start_time
        print(f"RSA Encryption Time for {size // (1024 * 1024)} MB: {rsa_encrypt_time:.4f} seconds")

        # Measure RSA decryption time
        start_time = time.time()
        rsa_decrypted_file_data = decrypt_file_rsa(rsa_private_key, rsa_encrypted_symmetric_key, rsa_encrypted_file_data)
        rsa_decrypt_time = time.time() - start_time
        print(f"RSA Decryption Time for {size // (1024 * 1024)} MB: {rsa_decrypt_time:.4f} seconds")

        # Measure ECC encryption time
        start_time = time.time()
        ecc_encrypted_file_data = encrypt_file_ecc(ecc_public_key, file_path)
        ecc_encrypt_time = time.time() - start_time
        print(f"ECC Encryption Time for {size // (1024 * 1024)} MB: {ecc_encrypt_time:.4f} seconds")

        # Measure ECC decryption time
        start_time = time.time()
        ecc_decrypted_file_data = decrypt_file_ecc(ecc_private_key, ecc_encrypted_file_data)
        ecc_decrypt_time = time.time() - start_time
        print(f"ECC Decryption Time for {size // (1024 * 1024)} MB: {ecc_decrypt_time:.4f} seconds")

if __name__ == "__main__":
    measure_performance()
 

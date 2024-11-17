from Crypto.Cipher import DES, AES
from Crypto.Util.Padding import pad, unpad
import time
import os

# Message to encrypt
message = "Performance Testing of Encryption Algorithms"
message_bytes = message.encode('utf-8')

# DES Encryption
def des_encrypt_decrypt(message):
    key = os.urandom(8)  # DES key must be 8 bytes
    start_time = time.time()
    cipher = DES.new(key, DES.MODE_CBC)
    iv = cipher.iv

    # Measure encryption time
    
    encrypted = cipher.encrypt(pad(message_bytes, DES.block_size))
    

    # Measure decryption time
    
    cipher_decrypt = DES.new(key, DES.MODE_CBC, iv)
    
    decrypted = unpad(cipher_decrypt.decrypt(encrypted), DES.block_size)
    des_time = time.time() - start_time

    return des_time

# AES-256 Encryption
def aes_encrypt_decrypt(message):
    key = os.urandom(32)  # AES key must be 32 bytes for AES-256
    start_time = time.time()
    cipher = AES.new(key, AES.MODE_CBC)
    iv = cipher.iv

    # Measure encryption time
    
    encrypted = cipher.encrypt(pad(message_bytes, AES.block_size))
    

    # Measure decryption time
    
    cipher_decrypt = AES.new(key, AES.MODE_CBC, iv)
    
    decrypted = unpad(cipher_decrypt.decrypt(encrypted), AES.block_size)
    aes_time = time.time() - start_time
    return aes_time

# Run the tests
des_times = des_encrypt_decrypt(message)
aes_times = aes_encrypt_decrypt(message)

# Print results
print(f"DES Encryption Time: {des_times:.6f} seconds")

print(f"AES-256 Encryption Time: {aes_times:.6f} seconds")


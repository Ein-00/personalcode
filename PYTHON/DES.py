from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import base64

key_string = "A1B2C3D4"
key = bytes(key_string,'utf-8')
cipher = DES.new(key, DES.MODE_ECB)  

plaintext = "Confidential Data".encode('utf-8')
plaintext_padded = pad(plaintext, DES.block_size) 

# Encrypt
ciphertext = cipher.encrypt(plaintext_padded)
print(ciphertext.hex())
ciphertext_b64 = base64.b64encode(ciphertext).decode('utf-8')
print("Ciphertext (Base64):", ciphertext_b64)

# Decrypt
cipher_decrypt = DES.new(key, DES.MODE_ECB)  # Create a new cipher for decryption
decrypted_padded = cipher_decrypt.decrypt(ciphertext)
decrypted = unpad(decrypted_padded, DES.block_size)  # Unpad the decrypted plaintext
decrypted_str = decrypted.decode('utf-8')
print("Decrypted:", decrypted_str)


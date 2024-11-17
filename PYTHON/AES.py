from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
import base64
key = b'0123456789ABCDEF0123456789ABCDEF'

cipher = AES.new(key, AES.MODE_ECB)

plaintext = b'Sensitive Information'
padded_plaintext = pad(plaintext, AES.block_size)

# Encrypt the plaintext
ciphertext = cipher.encrypt(padded_plaintext)
print(ciphertext)
ciphertext_b64 = base64.b64encode(ciphertext).decode('utf-8')
print("Ciphertext (Base64):", ciphertext_b64)

# Create the AES cipher object in decryption mode
cipher = AES.new(key, AES.MODE_ECB)

# Decrypt the ciphertext
decrypted_text = unpad(cipher.decrypt(ciphertext),AES.block_size)
print("Decrypted text:", decrypted_text.decode())

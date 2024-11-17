from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes
import base64

# Generate RSA keys
key = RSA.generate(2048)
private_key = key
public_key = key.publickey()

# Export keys to PEM format
private_key_pem = private_key.export_key()
public_key_pem = public_key.export_key()

# Message to encrypt
message = b"Asymmetric Encryption"

# Encrypt the message
cipher = PKCS1_OAEP.new(public_key)
ciphertext = cipher.encrypt(message)

print("Ciphertext:", ciphertext)
ciphertext_base64 = base64.b64encode(ciphertext)

print("Ciphertext (Base64):", ciphertext_base64.decode())
# Decrypt the message
cipher = PKCS1_OAEP.new(private_key)
decrypted_message = cipher.decrypt(ciphertext)

print("Decrypted message:", decrypted_message.decode())

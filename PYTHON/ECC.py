from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os
import base64

# Generate ECC private key
private_key = ec.generate_private_key(ec.SECP256R1(), default_backend())
public_key = private_key.public_key()

# Message to encrypt
message = b"Secure Transactions"

# Generate a shared secret using ECDH
peer_public_key = public_key  # In a real scenario, this would be the other party's public key
shared_secret = private_key.exchange(ec.ECDH(), peer_public_key)

# Derive a symmetric key from the shared secret
salt = os.urandom(16)  # Random salt for key derivation
kdf = Scrypt(
    salt=salt,
    length=32,
    n=2**14,
    r=8,
    p=1,
    backend=default_backend()
)
symmetric_key = kdf.derive(shared_secret)

# Encrypt the message using AES
iv = os.urandom(16)  # Initialization vector
cipher = Cipher(algorithms.AES(symmetric_key), modes.CFB(iv), backend=default_backend())
encryptor = cipher.encryptor()
ciphertext = encryptor.update(message) + encryptor.finalize()

# Convert to Base64 for easier display
ciphertext_base64 = base64.b64encode(ciphertext).decode()
iv_base64 = base64.b64encode(iv).decode()
salt_base64 = base64.b64encode(salt).decode()

print("IV (Base64):", iv_base64)
print("Ciphertext (Base64):", ciphertext_base64)

# Decrypt the message using the same symmetric key
cipher = Cipher(algorithms.AES(symmetric_key), modes.CFB(iv), backend=default_backend())
decryptor = cipher.decryptor()
decrypted_message = decryptor.update(ciphertext) + decryptor.finalize()

print("Decrypted message:", decrypted_message.decode())

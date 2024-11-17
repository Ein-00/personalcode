from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa , padding
from cryptography.hazmat.primitives import serialization , hashes
import base64


def generate_keys():
    # Generate a private key
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    # Generate the public key
    public_key = private_key.public_key()
    return private_key, public_key

def encrypt(public_key, message):
    # Encrypt the message
    ciphertext = public_key.encrypt(
        message.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return ciphertext

def decrypt(private_key, ciphertext):
    # Decrypt the message
    plaintext = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return plaintext.decode()

# Example usage

message = "Confidential Data"
print("Original Message:", message)

    # Generate keys
private_key, public_key = generate_keys()

    # Encrypt the message
ciphertext = encrypt(public_key, message)
ciphertext_base64= base64.b64encode(ciphertext).decode()
print("Ciphertext:", ciphertext_base64)

    # Decrypt the message
decrypted_message = decrypt(private_key, ciphertext)
print("Decrypted Message:", decrypted_message)

import streamlit as st
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
from connect import getdb


def derive_key(password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return kdf.derive(password.encode())


def decrypt_password(encrypted_data: str, key: bytes) -> str:
    try:
        decoded = base64.b64decode(encrypted_data)
        nonce, ciphertext, tag = decoded[:12], decoded[12:-16], decoded[-16:]
        cipher = Cipher(algorithms.AES(key), modes.GCM(nonce, tag), backend=default_backend())
        decryptor = cipher.decryptor()
        decrypted = decryptor.update(ciphertext) + decryptor.finalize()
        return decrypted.decode()
    except (ValueError, KeyError):
        return None


def login():
    st.title("Login Page")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    db = getdb()
    users_collection = db["userdata"]

    if st.button("Login"):
        user_data = users_collection.find_one({"username": username})
        if user_data:
            stored_password = user_data["password"]
            salt = base64.b64decode(user_data["salt"])

            derived_key = derive_key(password, salt)
            decrypted_password = decrypt_password(stored_password, derived_key)

            if decrypted_password == password:
                st.success("Login successful!")
                st.session_state.user = user_data
                return True
            else:
                st.error("Invalid username or password.")
        else:
            st.error("Invalid username or password.")
        return False


if __name__ == "__main__":
    if login():
        st.switch_page("pages/dashboard.py")
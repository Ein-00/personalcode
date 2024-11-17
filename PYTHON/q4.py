from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad, unpad

 # Define your DES keys
key1_des = bytes.fromhex('1234567890ABCDEF')
key2_des = bytes.fromhex('1234567890ABCDEF'[::-1])

# Create a Triple DES key by concatenating keys
key3_des = key1_des  # Reuse key1 for simplicity (2-key 3DES)
#
# # Initialize Triple DES cipher with the 3-key combination
key_triple_des = key1_des + key2_des + key3_des
cipher3des = DES3.new(key_triple_des, DES3.MODE_ECB)

# # Encryption
plaintext = "Classified Text".encode('utf-8')
padded_plaintext = pad(plaintext, DES3.block_size)
ciphertext = cipher3des.encrypt(padded_plaintext)
#
# # Decryption
decipher3des = DES3.new(key_triple_des, DES3.MODE_ECB)
decrypted_padded_plaintext = decipher3des.decrypt(ciphertext)
decrypted_plaintext = unpad(decrypted_padded_plaintext, DES3.block_size).decode('utf-8')
#
print("Ciphertext:", ciphertext.hex())
print("Decrypted Text:", decrypted_plaintext)

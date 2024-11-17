def encrypt(message, public_key):
    n, e = public_key
    encrypted_message = []
    for block in [message[i:i+4] for i in range(0, len(message), 4)]:
        block_value = 1
        for char in block:
            block_value *= ord(char)
        encrypted_block = pow(block_value, e, n)
        encrypted_message.append(encrypted_block)
    return encrypted_message

def decrypt(encrypted_message, private_key):
    n, d = private_key
    decrypted_message = []
    for block in encrypted_message:
        decrypted_block = pow(block, d, n)
        block_chars = []
        while decrypted_block > 0:
            block_chars.append(chr(decrypted_block % 256))
            decrypted_block //= 256
        decrypted_message.extend(reversed(block_chars))
    return ''.join(decrypted_message)

public_key = (3233, 17)
private_key = (3233, 2753)

message = "Asymmetric Encryption"
encrypted_message = encrypt(message, public_key)
print("Encrypted message:", encrypted_message)

decrypted_message = decrypt(encrypted_message, private_key)
print("Decrypted message:", decrypted_message)

def create_playfair_matrix(key):
    # Remove duplicates and create the matrix
    key = key.upper().replace("J", "I")
    seen = set()
    matrix = []
    
    for char in key:
        if char not in seen and char.isalpha():
            seen.add(char)
            matrix.append(char)
    
    # Fill the rest of the alphabet
    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in seen:
            seen.add(char)
            matrix.append(char)
    
    # Create a 5x5 matrix
    return [matrix[i:i + 5] for i in range(0, 25, 5)]

def prepare_message(message):
    message = message.upper().replace(" ", "").replace("J", "I")
    digraphs = []
    
    i = 0
    while i < len(message):
        if i + 1 < len(message):
            if message[i] == message[i + 1]:
                digraphs.append(message[i] + 'X')
                i += 1
            else:
                digraphs.append(message[i] + message[i + 1])
                i += 2
        else:
            digraphs.append(message[i] + 'X')
            i += 1
            
    return digraphs

def encipher_digraphs(digraphs, matrix):
    enciphered = []
    pos = {matrix[i][j]: (i, j) for i in range(5) for j in range(5)}
    
    for digraph in digraphs:
        row1, col1 = pos[digraph[0]]
        row2, col2 = pos[digraph[1]]
        
        if row1 == row2:  # Same row
            enciphered.append(matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5])
        elif col1 == col2:  # Same column
            enciphered.append(matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2])
        else:  # Rectangle
            enciphered.append(matrix[row1][col2] + matrix[row2][col1])
    
    return ''.join(enciphered)

# Main function to use the Playfair cipher
def playfair_cipher(key, message):
    matrix = create_playfair_matrix(key)
    digraphs = prepare_message(message)
    return encipher_digraphs(digraphs, matrix)

# Example usage
key = "GUIDANCE"
message = "The key is hidden under the door pad"
enciphered_message = playfair_cipher(key, message)
print("Enciphered Message:", enciphered_message)

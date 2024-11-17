
def move_max_to_upper_left(matrix):
    if not matrix or not matrix[0]:
        return matrix  # Return if the matrix is empty

    max_value = float('-inf')
    max_position = (0, 0)

    # Find the maximum value and its position
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] > max_value:
                max_value = matrix[i][j]
                max_position = (i, j)

    # Swap the maximum value with the upper left corner
    matrix[max_position[0]][max_position[1]], matrix[0][0] = matrix[0][0], matrix[max_position[0]][max_position[1]]

    return matrix

# Example usage
array = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

modified_array = move_max_to_upper_left(array)
print(modified_array)

def check_valid_coordinates(command_data, indices, matrix):
    if len(indices) == 4:
        row1, col1, row2, col2 = indices
        if (0 <= row1 < len(matrix) and 0 <= col1 < len(matrix[0]) and
                0 <= row2 < len(matrix) and 0 <= col2 < len(matrix[0])):
            return True

    print("Invalid input!")
    return False


def swap_value(command_data, indices, matrix_data):
    if command_data == 'swap':
        if check_valid_coordinates(command_data, indices, matrix_data):
            row1, col1, row2, col2 = indices
            matrix_data[row1][col1], matrix_data[row2][col2] = matrix_data[row2][col2], matrix_data[row1][col1]
            return matrix_data


rows, cols = [int(x) for x in input().split()]

matrix = [[x for x in input().split()] for _ in range(rows)]

while True:
    command = input().split()

    if command[0] == 'END':
        break

    coordinates = list(map(int, command[1:]))

    if command[0] == 'swap':
        result = swap_value(command[0], coordinates, matrix)
        if result:
            for row in matrix:
                print(' '.join(map(str, row)))

def check_valid_indices(indices, matrix_data):
    if 0 <= indices[0] < len(matrix_data) and 0 <= indices[1] < len(matrix_data[0]):
        return True
    else:
        print("Invalid coordinates")
        return False


def adding_value(command_data, indices):
    if command_data == 'Add':
        if check_valid_indices(indices, matrix):
            matrix[indices[0]][indices[1]] += indices[2]
        return matrix


def subtract_value(command_data, indices):
    if command_data == 'Subtract':
        if check_valid_indices(indices, matrix):
            matrix[indices[0]][indices[1]] -= indices[2]


rows = int(input())
matrix = [list(map(int, input().split())) for x in range(rows)]

while True:

    command = input().split()

    if command[0] == 'END':
        break

    coordinates = list(map(int, command[1:]))

    if command[0] == 'Add':
        adding_value(command[0], coordinates)
    elif command[0] == 'Subtract':
        subtract_value(command[0], coordinates)


for row in matrix:
    print(' '.join(map(str, row)))
rows, cols = [int(x) for x in input().split()]
matrix = [input().split() for _ in range(rows)]


squared_matrix_count = 0

for row in range(rows - 1):
    for col in range(cols - 1):
        letter = matrix[row][col]

        if letter == matrix[row + 1][col] and letter == matrix[row][col + 1] and letter == matrix[row + 1][col + 1]:
            squared_matrix_count += 1

print(squared_matrix_count)
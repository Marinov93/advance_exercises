import sys

rows , columns = [int(x) for x in input().split(", ")]

matrix = []

for row in range(rows):
    data = [int(y) for y in input().split(", ")]
    matrix.append(data)

max_num = 0
matrix_count = []

for i in range(rows - 1):
    for j in range(columns - 1):
        element = matrix[i][j]
        next_element = matrix[i][j + 1]
        element_below = matrix[i + 1][j]
        other_element = matrix[i + 1][j + 1]

        total_sum = element + next_element + element_below + other_element

        if total_sum > max_num:
            max_num = total_sum
            matrix_count = [[element, next_element], [element_below, other_element]]


print(*matrix_count[0])
print(*matrix_count[1])
print(max_num)
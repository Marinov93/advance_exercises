number = int(input())
matrix = []
for i in range(number):
    # data = [int(x) for x in input().split(', ')]
    data = [int(x) for x in input().split(', ') if int(x) % 2 == 0]
    matrix.append(data)
print(matrix)

# even_matrix = []
# for row in range(len(matrix)):
#     even_matrix.append([])
#     for col in range(len(matrix[row])):
#         if matrix[row][col] % 2 == 0:
#             even_matrix[row].append(matrix[row][col])

# print(even_matrix)
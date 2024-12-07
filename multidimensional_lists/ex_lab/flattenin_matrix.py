rows = int(input())

matrix = []
flat_result = []
# for col in range(rows):
#     matrix.append(col)
#
# print([int(col) for row in matrix for col in input().split(', ')])

for i in range(rows):
    row_data = [int(x) for x in input().split(', ')]
    matrix.append(row_data)
    flat_result.extend(row_data)

print(flat_result)


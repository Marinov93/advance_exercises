rows, columns = [int(x) for x in input().split(", ")]

matrix = []

for row in range(rows):
    data = [int(y) for y in input().split()]
    matrix.append(data)
for j in range(columns):
    sum_total = sum(matrix[row][j] for row in range(rows))
    print(sum_total)

number_n = int(input())

matrix = []

for i in range(number_n):
    data = list(input())
    matrix.append(data)

symbol_data = input()



for row in range(number_n):
    for col in range(number_n):
        if matrix[row][col] == symbol_data:
            print(f"({row}, {col})")
            exit()

print(f"{symbol_data} does not occur in the matrix")
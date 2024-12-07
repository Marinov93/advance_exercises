rows, columns = [int(x) for x in input().split(', ')]

matrix = []
sum_nums = 0
for i in range(rows):
    numbers = [int(x) for x in input().split(', ')]
    matrix.append(numbers)
    sum_nums += sum(numbers)


print(sum_nums)
print(matrix)

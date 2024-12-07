number = int(input())

matrix = [[int(el) for el in input().split()] for _ in range(number)]
primary = [matrix[x][x] for x in range(number)]
second = [matrix[j][number - j - 1] for j in range(number)]

primary_count = 0
second_count = 0

for y in primary:
    primary_count += y
for j in second:
    second_count += j

print(abs(primary_count - second_count))
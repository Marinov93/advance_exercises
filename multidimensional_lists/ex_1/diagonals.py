number = int(input())

matrix = [[int(el) for el in input().split(', ')] for _ in range(number)]
primary = [matrix[x][x] for x in range(number)]
second = [matrix[j][number - j - 1] for j in range(number)]

print(f"Primary diagonal: {', '.join(str(x) for x in primary)}. Sum: {sum(primary)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in second)}. Sum: {sum(second)}")
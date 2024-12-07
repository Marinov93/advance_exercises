rows, cols = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for _ in range(rows)]

max_num = float("-inf")

biggest_matrix = []

for row in range(rows - 2):
    for col in range(cols - 2):
        first_nums = matrix[row][col:col + 3]
        second_nums = matrix[row + 1][col:col + 3]
        third_nums = matrix[row + 2][col:col + 3]

        sum_nums = sum(first_nums) + sum(second_nums) + sum(third_nums)
        if sum_nums > max_num:
            max_num = sum_nums
            biggest_matrix = [first_nums, second_nums, third_nums]


print(f"Sum = {max_num}")
[print(*row) for row in biggest_matrix]
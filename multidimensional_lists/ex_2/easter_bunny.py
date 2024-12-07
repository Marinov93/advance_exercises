size = int(input())
eggs_map = [[x for x in input().split()] for _ in range(size)]

max_eggs = float("-inf")
direction = ''
eggs_matrix = []
bunny_position = []
current_egg_matrix = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(size):
    for col in range(size):
        if eggs_map[row][col] == 'B':
            bunny_position = [row, col]

for way, move in directions.items():
    eggs = 0  # Reset egg count for each direction
    move_row = bunny_position[0] + move[0]
    move_col = bunny_position[1] + move[1]

    while 0 <= move_row < size and 0 <= move_col < size:
        if eggs_map[move_row][move_col] == "X":
            break
        eggs += int(eggs_map[move_row][move_col])
        current_egg_matrix.append([move_row, move_col])
        move_row += move[0]
        move_col += move[1]

    if eggs > max_eggs and current_egg_matrix:
        max_eggs = eggs
        direction = way
        eggs_matrix = current_egg_matrix

print(direction)
[print(row) for row in eggs_matrix]
print(max_eggs)

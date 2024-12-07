def counter_terrorist_moving(counter_terrorist_position_data, command, bomb_time_data):
    if bomb_time_data:
        movement = directions[command]
        new_row = counter_terrorist_position_data[0] + movement[0]
        new_col = counter_terrorist_position_data[1] + movement[1]
        return new_row, new_col, bomb_time_data
    return counter_terrorist_position_data[0], counter_terrorist_position_data[1], bomb_time_data


row, col = [int(x) for x in input().split(", ")]

# matrix with "C" letter shows counter terrorist , "B" shows bomb on map , "T" shows terrorist

matrix = []
bomb_time = 16
counter_terrorist_position = []
bomb_position = []
terrorist_position = []
defused_bomb = False
killed = False

for r in range(row):
    lines = list(input())
    matrix.append(lines)

    if "C" in lines:
        counter_terrorist_position = [r, lines.index("C")]

    if "B" in lines:
        bomb_position = [r, lines.index("B")]

    # if "T" in lines:
    #     terrorist_position = [r, lines.index("T")]


directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
}

while bomb_time and not defused_bomb and not killed:
    commands = input()
    if commands in directions: # when valid command is given
        bomb_time -= 1 # time ticking
        new_row, new_col, bomb_time = counter_terrorist_moving(counter_terrorist_position, commands, bomb_time) # update position
        if 0 <= new_row < row and 0 <= new_col < col:
            counter_terrorist_position = [new_row, new_col]
            if matrix[new_row][new_col] == "T":
                killed = True
                matrix[new_row][new_col] = "*"
                break
        else:
            bomb_time -= 1
            continue

    elif commands == 'defuse':
        if counter_terrorist_position != bomb_position:
            bomb_time -= 2
            continue
        # elif counter_terrorist_position == bomb_position:
        else:
            if bomb_time > 4:
                bomb_time -= 4
                matrix[bomb_position[0]][bomb_position[1]] = 'D'
                defused_bomb = True
            else:
                matrix[bomb_position[0]][bomb_position[1]] = 'X'
                killed = True


if defused_bomb and bomb_time:
    print("Terrorists win!")
    print("Bomb was not defused successfully!")
    print(f"Time needed: {bomb_time} second/s.")

if defused_bomb:
    print("Counter-terrorist wins!")
    print(f"Bomb has been defused: {bomb_time} second/s remaining.")

if killed:
    print("Terrorists win!")

for el in matrix:
    print("".join(el))



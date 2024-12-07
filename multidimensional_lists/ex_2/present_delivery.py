# matrix -> if cell with "X" naughty kid , #V for nice kid , "C" for cookie and "-" empty cell
def eat_cookie(presents_left, nice_kids_number):
    for coord in directions.values():
        r = santa_position[0] + coord[0]
        c = santa_position[1] + coord[1]

        if matrix[r][c].isalpha():
            if matrix[r][c] == 'V':
                nice_kids_number += 1

            matrix[r][c] = '-'
            presents_left -= 1

        if not presents_left:
            break

    return presents_left, nice_kids_number


santa_presents = int(input())

matrix_size = int(input())

matrix = []
santa_position = []

nice_kids = 0
total_nice_kids = 0

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
}

for row in range(matrix_size):
    lines = list(input().split())
    matrix.append(lines)
    if "S" in lines:
        santa_position = [row, lines.index("S")]
        matrix[row][santa_position[1]] = '-'

    total_nice_kids += lines.count("V")

while True:
    command = input()
    if command == 'Christmas morning':
        break

    santa_position = [santa_position[0] + directions[command][0], santa_position[1] + directions[command][1]]

    house = matrix[santa_position[0]][santa_position[1]]

    if house == 'V':
        nice_kids += 1
        santa_presents -= 1
    elif house == 'C':
        santa_presents, nice_kids = eat_cookie(santa_presents, nice_kids)

    matrix[santa_position[0]][santa_position[1]] = '-'

    if not santa_presents or nice_kids == total_nice_kids:
        break

matrix[santa_position[0]][santa_position[1]] = 'S'

if not santa_presents and nice_kids < total_nice_kids:
    print("Santa ran out of presents!")

print(*[' '.join(line) for line in matrix], sep='\n')

if total_nice_kids == nice_kids:
    print(f'Good job, Santa! {nice_kids} happy nice kid/s.')
else:
    print(f'No presents for {total_nice_kids - nice_kids} nice kid/s.')



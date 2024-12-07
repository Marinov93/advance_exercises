size = int(input()) # matrix size
matrix = [list(input()) for _ in range(size)] # matrix with items

positions = (
    (-2, -1), #горе 2, ляво 1
    (-2, 1),  #горе 2 , дясно 1
    (-1, -2), #горе 1 , ляво 2
    (-1, 2),  #горе 1, дясно 2
    (2, 1),   #долу 2, дясно 1
    (2, -1),  #долу 2 ляво 1
    (1, -2),  #долу 1, ляво 2
    (1, 2),   #долу 1, ляво 2
)


removed_knights = 0

while True:
    max_attacks = 0
    knights_max_attacks = []

    for row in range(size): # looping over matrix
        for col in range(size): # looping over matrix
            if matrix[row][col] == 'K': # we need to find the position of knight
                attacks = 0

                for pos in positions: # looping over positions to find where is knight going
                    pos_row = row + pos[0]
                    pos_col = col + pos[1]

                    if 0 <= pos_row < size and 0 <= pos_col < size: # to find if in this spot there is knight to attack
                        if matrix[pos_row][pos_col] == 'K':
                            attacks += 1

                if attacks > max_attacks:
                    knights_max_attacks = [row, col] # saving knight with most attacks.
                    max_attacks = attacks

    if knights_max_attacks:
        r, c = knights_max_attacks
        matrix[r][c] = '0'
        removed_knights += 1
    else:
        break

print(removed_knights)
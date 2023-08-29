def get_possible_attack_coords(matrix_chess, row, col):
    possible_moves = [
        [row - 2, col + 1],
        [row - 2, col - 1],
        [row - 1, col - 2],
        [row - 1, col + 2],
        [row + 1, col - 2],
        [row + 1, col + 2],
        [row + 2, col - 1],
        [row + 2, col + 1],
]

    result = []

    for moves_row, moves_col in possible_moves:
        if 0 <= moves_row < len(matrix_chess) and 0 <= moves_col < len(matrix_chess) and matrix_chess[moves_row][moves_col] == "K":
            result.append([moves_row, moves_col])

    return result

size = int(input())
matrix = []
knight_cells = []
max_damage = 0
current_knight_damage = 0
removed_knights = 0
most_dangerous_knight = []

for row in range(size):
    matrix.append(list(input()))
    for col in range(size):
        if matrix[row][col] == "K":
            knight_cells.extend([f"{row} {col}"])

while True:

    for cell in knight_cells:
        knight_row, knight_col = [int(x) for x in cell.split()]
        current_knight_moves_list = get_possible_attack_coords(matrix, knight_row, knight_col)
        current_knight_damage = len(current_knight_moves_list)

        if current_knight_damage > max_damage:
            max_damage = current_knight_damage
            most_dangerous_knight = cell
            most_dangerous_knight_row = knight_row
            most_dangerous_knight_col = knight_col

    if max_damage == 0:
        break

    else:
        knight_cells.remove(most_dangerous_knight)
        matrix[most_dangerous_knight_row][most_dangerous_knight_col] = "0"
        removed_knights += 1
        max_damage = 0

print(removed_knights)















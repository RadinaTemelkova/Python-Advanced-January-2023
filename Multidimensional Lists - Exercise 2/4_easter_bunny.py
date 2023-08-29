size = int(input())
matrix = []
bunny_start_coords = []
collected_eggs = 0
greatest_number_of_eggs = float("-inf")
best_direction_cells = []
current_direction_cells = []
best_direction = ""

for row in range(size):
    matrix.append(list(input().split()))
    for col in range(size):
        if matrix[row][col] == "B":
            bunny_start_coords.extend([row, col])

directions = {
    "up": [- 1, 0],
    "down": [1, 0],
    "left": [0, - 1],
    "right": [0, 1],
}

for direction, coordinates in directions.items():

    current_row, current_col = bunny_start_coords[0] + directions[direction][0], bunny_start_coords[1] + directions[direction][1]

    while True:

        if 0 <= current_row < size and 0 <= current_col < size and matrix[current_row][current_col] != "X":

            collected_eggs += int(matrix[current_row][current_col])
            current_direction_cells.append([current_row, current_col])
            current_row, current_col = current_row + directions[direction][0], current_col + directions[direction][1]

        else:
            if collected_eggs > greatest_number_of_eggs and current_direction_cells:

                greatest_number_of_eggs = collected_eggs
                best_direction = direction
                best_direction_cells = current_direction_cells.copy()

            current_direction_cells.clear()
            collected_eggs = 0

print(f"{best_direction}")

for row in range(len(best_direction_cells)):
    print(best_direction_cells[row])

print(f"{greatest_number_of_eggs}")
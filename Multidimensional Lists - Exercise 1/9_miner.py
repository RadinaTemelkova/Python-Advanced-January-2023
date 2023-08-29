size = int(input())
commands = input().split()
matrix = [[char for char in input().split()] for row in range(size)]
total_coal = 0
game_over = False

# print(matrix)

commands_dict = {
    "left": [0, -1],
    "right": [0, 1],
    "up": [-1, 0],
    "down": [1, 0]
}

for row in range(size):
    for col in range(size):
        if matrix[row][col] == "s":
            curr_position = [row, col]

        elif matrix[row][col] == "c":
            total_coal += 1

for current_command in commands:

    if current_command in commands_dict.keys():
        row_dir = commands_dict[current_command][0]
        col_dir = commands_dict[current_command][1]

        r, c = curr_position[0] + row_dir, curr_position[1] + col_dir

        if not (0 <= r < size and 0 <= c < size):
            continue

        else:
            if matrix[r][c] == "e":
                game_over = True
                break

            elif matrix[r][c] == "*":
                curr_position = r, c
                continue

            elif matrix[r][c] == "c":
                matrix[r][c] = "*"
                total_coal -= 1
                if total_coal == 0:
                    game_over = True
                    break
                curr_position = r, c


if game_over:
    if total_coal == 0:
        print(f"You collected all coal! ({r}, {c})")
    else:
        print(f"Game over! ({r}, {c})")

else:
    print(f"{total_coal} pieces of coal left. ({r}, {c})")











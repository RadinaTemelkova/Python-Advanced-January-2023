size = 5
matrix = []
total_targets = 0
shot_targets = 0
shot_targets_list = []
a_row, a_col = 0, 0
all_targets_shot = False

for row in range(size):
    matrix.append(list(input().split()))
    for col in range(size):
        if matrix[row][col] == "A":
            a_row = row
            a_col = col
        elif matrix[row][col] == "x":
            total_targets += 1

number_of_commands = int(input())

directions = {
    "up": (- 1, 0),
    "down": (1, 0),
    "left": (0, - 1),
    "right": (0, 1),
}

for x in range(number_of_commands):
    command = input().split()
    action = command[0]
    direction = command[1]

    if action == "move":
        steps = int(command[2])
        new_row = a_row + directions[direction][0] * steps
        new_col = a_col + directions[direction][1] * steps
        if 0 <= new_row < size and 0 <= new_col < size:
            if matrix[new_row][new_col] == ".":
                matrix[a_row][a_col] = "."
                matrix[new_row][new_col] = "A"
                a_row, a_col = new_row, new_col

    elif action == "shoot":
        new_shoot_row = a_row + directions[direction][0]
        new_shoot_col = a_col + directions[direction][1]

        while 0 <= new_shoot_row < size and 0 <= new_shoot_col < size:
            if matrix[new_shoot_row][new_shoot_col] == "x":
                shot_targets += 1
                shot_targets_list.append([new_shoot_row, new_shoot_col])
                matrix[new_shoot_row][new_shoot_col] = "."
                if shot_targets == total_targets:
                    all_targets_shot = True
                break
            new_shoot_row, new_shoot_col = new_shoot_row + directions[direction][0], new_shoot_col + directions[direction][1]

        if all_targets_shot:
            break

if all_targets_shot:
    print(f"Training completed! All {total_targets} targets hit.")
else:
    print(f"Training not completed! {total_targets - shot_targets} targets left.")
print(*shot_targets_list, sep="\n")
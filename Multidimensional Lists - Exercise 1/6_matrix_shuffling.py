def valid_input_func(curr_command):

    current_command = curr_command.split()
    input_is_valid = False

    if current_command[0] == "swap" and len(current_command) == 5:
        row1, col1, row2, col2 = [int(x) for x in current_command[1:]]

        if 0 <= row1 < rows and 0 <= row2 < rows and 0 <= col1 < cols and 0 <= col2 < cols:
            input_is_valid = True
            matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]

    return input_is_valid


rows, cols = [int(x) for x in input().split()]
matrix = [[x for x in input().split()] for row in range(rows)]

while True:
    command = input()

    if command == "END":
        break

    if not valid_input_func(command):
        print("Invalid input!")
        continue

    else:
        for row in matrix:
            print(*row, sep=" ")

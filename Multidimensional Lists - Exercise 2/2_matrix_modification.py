size = int(input())
matrix = [[el for el in input().split()] for row in range(size)]

while True:
    commands = input()
    if commands == "END":
        for row in matrix:
            print(" ".join(row))
        break

    action, *num_data = commands.split()

    row, col, value = [int(num) for num in num_data]

    if 0 <= row < size and 0 <= col < size:
        current_number = int(matrix[row][col])
        if action == "Add":
            current_number += value

        elif action == "Subtract":
            current_number -= value

        matrix[row][col] = str(current_number)
    else:
        print("Invalid coordinates")
        continue










rows, cols = [int(x) for x in input().split()]
matrix = []

for row in range(rows):
    matrix.append([])
    for col in range(cols):
        first_letter = last_letter = chr(97 + row)
        middle_letter = chr(97 + col + row)
        matrix[row].append(f"{first_letter}{middle_letter}{last_letter}")

[print(*row) for row in matrix]


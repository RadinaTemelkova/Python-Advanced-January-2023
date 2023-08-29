rows, cols = [int(x) for x in input().split()]
matrix = [[y for y in input().split()] for row in range(rows)]
number_of_square_matrices = 0

for row in range(rows - 1):
    for col in range(cols - 1):
        if matrix[row][col] == matrix[row][col + 1] == matrix[row + 1][col] == matrix[row + 1][col + 1]:
            number_of_square_matrices += 1

print(number_of_square_matrices)

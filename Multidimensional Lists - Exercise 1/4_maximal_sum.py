rows, cols = [int(x) for x in input().split()]
matrix = [[int(y) for y in input().split()] for row in range(rows)]

max_submatrix_sum = float("-inf")
submatrix_sum = 0
greatest_submatrix = []

for row in range(rows - 2):
    for col in range(cols - 2):
        first_subrow = matrix[row][col:col + 3]
        second_subrow = matrix[row + 1][col:col + 3]
        third_subrow = matrix[row + 2][col:col + 3]

        submatrix_sum = sum(first_subrow) + sum(second_subrow) + sum(third_subrow)

        if submatrix_sum > max_submatrix_sum:
            max_submatrix_sum = submatrix_sum
            greatest_submatrix = [first_subrow, second_subrow, third_subrow]

print(f"Sum = {max_submatrix_sum}")

for row in greatest_submatrix:
    print(*row, sep=" ")


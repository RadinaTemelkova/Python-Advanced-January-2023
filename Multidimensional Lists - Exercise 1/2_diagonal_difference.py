size = int(input())
matrix = [[int(x) for x in input().split()] for row in range(size)]
primary_diagonal = []
secondary_diagonal = []

for row in range(size):
    primary_element = matrix[row][row]
    primary_diagonal.append(primary_element)

    secondary_element = matrix[row][size - row - 1]
    secondary_diagonal.append(secondary_element)

diff = abs(sum(primary_diagonal) - sum(secondary_diagonal))
print(diff)



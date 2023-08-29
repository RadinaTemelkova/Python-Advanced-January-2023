size = int(input())
matrix = [[int(x) for x in input().split(", ")] for row in range(size)]
primary_diagonal = []
secondary_diagonal = []

for row in range(size):
    primary_element = matrix[row][row]
    primary_diagonal.append(primary_element)

    secondary_element = matrix[row][size - row - 1]
    secondary_diagonal.append(secondary_element)

print(f"Primary diagonal: {', '.join([str(el) for el in primary_diagonal])}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join([str(el) for el in secondary_diagonal])}. Sum: {sum(secondary_diagonal)}")



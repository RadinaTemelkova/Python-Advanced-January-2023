string = input()
matrix = [[print(el, end=" ") for el in row.split()] for row in string.split("|")[::-1]]

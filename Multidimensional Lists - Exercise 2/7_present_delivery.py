presents_count = int(input())
neighbourhood_size = int(input())
neighbourhood = []
nice_kids = 0
happy_nice_kids = 0
santa_row, santa_col = 0, 0

for row in range(neighbourhood_size):
    neighbourhood.append(list(input().split()))
    nice_kids += neighbourhood[row].count("V")
    for col in range(neighbourhood_size):
        if neighbourhood[row][col] == "S":
            santa_row, santa_col = row, col

directions = {
    "up": (- 1, 0),
    "down": (1, 0),
    "left": (0, - 1),
    "right": (0, 1),
}

while presents_count > 0:
    command = input()
    if command == "Christmas morning":
        break
    if command in directions.keys():
        new_row, new_col = santa_row + directions[command][0], santa_col + directions[command][1]
    if not(0 <= new_row < neighbourhood_size and 0 <= new_col < neighbourhood_size):
        continue

    neighbourhood[santa_row][santa_col] = "-"

    if neighbourhood[new_row][new_col] == "C":
        for direction in directions.keys():
            kid_row, kid_col = new_row + directions[direction][0], new_col + directions[direction][1]
            if neighbourhood[kid_row][kid_col] != "-":
                presents_count -= 1
                if neighbourhood[kid_row][kid_col] == "V":
                    happy_nice_kids += 1
            neighbourhood[kid_row][kid_col] = "-"
    elif neighbourhood[new_row][new_col] == "V":
        presents_count -= 1
        happy_nice_kids += 1

    neighbourhood[new_row][new_col] = "S"
    santa_row, santa_col = new_row, new_col

if presents_count == 0 and nice_kids - happy_nice_kids > 0:
    print(f"Santa ran out of presents!")
[print(*row) for row in neighbourhood]
if nice_kids == happy_nice_kids:
    print(f"Good job, Santa! {nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids - happy_nice_kids} nice kid/s.")



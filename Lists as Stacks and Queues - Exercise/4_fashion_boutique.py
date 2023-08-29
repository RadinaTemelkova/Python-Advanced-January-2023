clothes = [int(x) for x in input().split()]
capacity_per_rack = int(input())
sum_of_values = 0
number_of_racks = 1

for y in range(len(clothes.copy())):
    current_piece_value = clothes.pop()
    if sum_of_values + current_piece_value > capacity_per_rack:
        number_of_racks += 1
        sum_of_values = current_piece_value
    elif sum_of_values + current_piece_value == capacity_per_rack and clothes:
        number_of_racks += 1
        sum_of_values = 0
    else:
        sum_of_values += current_piece_value
print(number_of_racks)


def even_odd(*data):
    command = data[-1]
    if command == "even":
        numbers_list = list(filter(lambda x: x % 2 == 0, data[:-1]))
    elif command == "odd":
        numbers_list = list(filter(lambda x: x % 2 != 0, data[:-1]))
    return numbers_list

print(even_odd(1, 2, 3, 4, 5, 6, "even"))
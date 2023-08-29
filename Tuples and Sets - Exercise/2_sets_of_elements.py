first_set_length, second_set_length = [int(x) for x in input().split()]
first_set = set()
second_set = set()

for y in range(first_set_length):
    first_set.add(int(input()))

for z in range(second_set_length):
    second_set.add(int(input()))

print(*(first_set.intersection(second_set)), sep="\n")


count_of_lines = int(input())
set_of_elements = set()

for x in range(count_of_lines):
    elements = input().split()
    for element in elements:
        set_of_elements.add(element)

print(*set_of_elements, sep="\n")


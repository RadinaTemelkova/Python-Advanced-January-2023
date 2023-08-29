number_of_lines = int(input())
numbers_stack = []

for x in range(number_of_lines):
    command = input()

    if command.startswith("1"):
        action = command.split()
        number_to_push = int(action[1])
        numbers_stack.append(number_to_push)

    elif command == "2" and numbers_stack:
        numbers_stack.pop()

    elif command == "3" and numbers_stack:
        print(max(numbers_stack))

    elif command == "4" and numbers_stack:
        print(min(numbers_stack))

list_of_elements = []
for index in range(len(numbers_stack)-1, -1, -1):
    element = numbers_stack.pop()
    list_of_elements.append(str(element))

print(", ".join(list_of_elements))


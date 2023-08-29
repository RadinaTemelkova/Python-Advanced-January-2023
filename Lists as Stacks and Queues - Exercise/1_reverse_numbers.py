numbers_stack = input().split()

for index in range(len(numbers_stack)):
    element = numbers_stack.pop()
    print(element, end=" ")

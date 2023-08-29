def func_executor(*args):
    result = []
    for func_name, func_arguments in args:
        result.append(f"{func_name.__name__} - {func_name(*func_arguments)}")

    return "\n".join(result)


def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


print(func_executor(
    (sum_numbers, (1, 2)),
    (multiply_numbers, (2, 4))
))

def concatenate(*some_strings, **named_arguments):

    concatenated_strings = "".join(some_strings)

    for key, value in named_arguments.items():
        concatenated_strings = concatenated_strings.replace(key, value)

    return "".join(concatenated_strings)


print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))
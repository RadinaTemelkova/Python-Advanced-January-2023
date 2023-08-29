some_text = input()
chars_dict = {}

for char in some_text:
    if char not in chars_dict.keys():
        chars_dict[char] = 0
    chars_dict[char] += 1

sorted_chars_dict = dict(sorted(chars_dict.items()))

for key, value in sorted_chars_dict.items():
    print(f"{key}: {value} time/s")




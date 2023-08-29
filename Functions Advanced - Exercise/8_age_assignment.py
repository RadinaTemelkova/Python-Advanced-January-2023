def age_assignment(*names, **person_data):
    result = []
    for name in names:
        first_letter = name[0]
        if first_letter in person_data.keys():
            age = person_data[first_letter]
            result.append(f"{name} is {age} years old.")

    sorted_result = sorted(result, key=lambda x: x[0])
    return "\n".join(sorted_result)


print(age_assignment("Peter", "George", G=26, P=19))
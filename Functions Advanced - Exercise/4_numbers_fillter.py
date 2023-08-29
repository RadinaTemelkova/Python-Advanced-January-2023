def even_odd_filter(**kwargs):
    sorted_dict = {}
    for key in kwargs.keys():
        if key == "odd":
            filtered_list = list(filter(lambda x: x % 2 != 0, kwargs[key]))
        elif key == "even":
            filtered_list = list(filter(lambda x: x % 2 == 0, kwargs[key]))
        if key not in sorted_dict.keys():
            sorted_dict[key] = []
        sorted_dict[key].extend(filtered_list)

    return dict(sorted(sorted_dict.items(), key=lambda item: -len(item[1])))


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))

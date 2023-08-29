def grocery_store(**products):
    result = []
    sorted_data = sorted(products.items(), key=lambda x: (-(int(x[1])), -len(x[0]), x[0]))

    for el in sorted_data:
        result.append(f"{el[0]}: {el[1]}")
    return "\n".join(result)


print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))

def fill_the_box(height, length, width, *cubes_data):
    cubes_left = 0
    box_size = height * length * width

    for cubes in cubes_data:
        if cubes == "Finish":
            break

        if box_size - cubes > 0:
            box_size -= cubes

        elif box_size - cubes <= 0:
            cubes -= box_size
            cubes_left += cubes
            box_size = 0

        elif box_size == 0:
            cubes_left += cubes

    if box_size > 0:
        return f"There is free space in the box. You could put {box_size} more cubes."
    else:
        return f"No more free space! You have {cubes_left} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))


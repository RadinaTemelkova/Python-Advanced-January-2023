intersection = []

for x in range(int(input())):
    first_set = set()
    second_set = set()

    first_range, second_range = [z for z in input().split("-")]

    first_start, first_end = first_range.split(",")
    second_start, second_end = second_range.split(",")

    for q in range(int(first_start), int(first_end)+1):
        first_set.add(q)
    for z in range(int(second_start), int(second_end)+1):
        second_set.add(z)
    intersection.append(first_set.intersection(second_set))

longest_intersection = (list(max(intersection, key = len)))
print(f"Longest intersection is {longest_intersection} with length {len(longest_intersection)}")


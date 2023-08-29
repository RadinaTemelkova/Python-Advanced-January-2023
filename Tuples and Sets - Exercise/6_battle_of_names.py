number_of_names = int(input())
odd_results = set()
even_results = set()

for x in range(1, number_of_names + 1):
    result = 0
    current_name = input()
    for letter in current_name:
        result += ord(letter)
    result = result // x

    if result % 2 == 0:
        even_results.add(result)
    else:
        odd_results.add(result)

if sum(odd_results) == sum(even_results):
    print(*(odd_results.union(even_results)), sep=", ")

elif sum(odd_results) > sum(even_results):
    print(*(odd_results.difference(even_results)), sep=", ")

else:
    print(*(even_results.symmetric_difference(odd_results)), sep=", ")


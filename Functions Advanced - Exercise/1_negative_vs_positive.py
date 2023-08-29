def total_sum_func(list_of_numbers):
    sum_of_positives = 0
    sum_of_negatives = 0
    for number in list_of_numbers:
        if int(number) > 0:
            sum_of_positives += int(number)
        else:
            sum_of_negatives += int(number)
    return sum_of_positives, sum_of_negatives


numbers = input().split()
positives, negatives = total_sum_func(numbers)
print(negatives)
print(positives)
if positives > abs(negatives):
    print("The positives are stronger than the negatives")
else:
    print("The negatives are stronger than the positives")


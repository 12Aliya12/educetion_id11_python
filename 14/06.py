def print_average(numbers):
    sum_obshiy = 0
    if len(numbers) == 0:
        print(0)
    else:
        for i in numbers:
            sum_obshiy += int(i)
        sred_znach = sum_obshiy / len(numbers)
        print(sred_znach)


numbers = list(input().split())
print_average(numbers)
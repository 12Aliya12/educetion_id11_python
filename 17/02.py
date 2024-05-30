daily_food = [0, 150, 150]


def count_food(lst: list):
    total_food = 0
    for i in lst:
        if i > 0:
            total_food += daily_food[i - 1]
        return total_food


print(count_food([1]))
print(count_food([2, 3]))
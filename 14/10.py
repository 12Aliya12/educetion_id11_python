def golden_ratio(i):
    chsilo_one = 1
    chislo_two = 1
    for j in range(i - 1):
        chsilo_one, chislo_two = chislo_two, chsilo_one + chislo_two
    print(chislo_two / chsilo_one)


i = int(input())
golden_ratio(i)
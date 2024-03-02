chislo= 1
summ = 0
number_string = 0
vivod_summ_ten_string = 0
sum_ten = False
while chislo != 0:
    chislo = int(input("Введите число: "))
    summ += chislo
    number_string+= 1
    if summ == 10:
        sum_ten = True
        if sum_ten:
            vivod_summ_ten_string = number_string
print(vivod_summ_ten_string)
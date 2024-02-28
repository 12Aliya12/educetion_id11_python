chislo = int(input("Введите число: "))
nach = 0
for i in range( chislo):
    chislo2 = int(input("Введите число: "))
    if i % 2 != 0:
        nach -= chislo2
    else:
        nach += chislo2
print("Сумма равна: ", nach)
d = int(input("Введите число: "))
for i in range(17):
    if i % d == 0:
        print(d, "ДА")
        d = int(input("Введите число: "))
    else:
        print(d, "НЕТ")
        d = int(input("Введите число: "))

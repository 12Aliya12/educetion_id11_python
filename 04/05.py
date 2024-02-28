chislo = int(input("Введите число: "))
proiz = 1
for i in range(6):
    if chislo == 0:
        chislo == 1
    else:
        proiz *= chislo
    chislo = int(input("Введите число: "))
print(proiz)
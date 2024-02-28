chislo = int(input("Введите число: "))
delit = 1
for i in range(chislo + 1):
    if chislo % delit == 0:
        print(delit, end=' ')
        delit += 1
    else:
        delit += 1
print(end='\n')
if not(chislo / 2) and not (chislo / 3) and chislo/chislo:
    print("Простое")
else:
    print("НЕТ")
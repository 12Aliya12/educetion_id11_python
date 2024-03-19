slovo = input()
chislo = int(input())
if len(slovo) > chislo:
    print(slovo[chislo - 1])
else:
    print("ОШИБКА")
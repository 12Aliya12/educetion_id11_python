stroka = list()
for i in range(int(input())):
    stroka.append(input())
poziciya = int(input())
for i in stroka:
    print(i[poziciya-1], end="")
stroka = list()
for i in range(int(input())):
    stroka.append(input())
poisk_storka = input()
for i in stroka:
    if poisk_storka in i:
        print(i)

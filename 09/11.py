beliy_spisok = list()
for i in range(int(input())):
    beliy_spisok.append(input())
spisok_zaprosov = list()
for k in range(int(input())):
    spisok_zaprosov.append((input()))
for i in spisok_zaprosov:
    flagok = True
    for k in beliy_spisok:
        if k not in i:
            flagok = False
    if flagok:
        print(i)
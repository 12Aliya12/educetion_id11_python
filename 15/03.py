def take_large_banknotes(banknotes):
    vivod = list()
    for i in banknotes:
        if float(i) > 10:
            vivod.append(i)
    print(*vivod, end=" ")


banknotes = list(input().split())
take_large_banknotes(banknotes)
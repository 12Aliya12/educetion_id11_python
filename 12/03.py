spisok_chisel = [int(i) for i in input().split()]
oblast_raboty = [int(i) for i in input().split()]
otvet = 0
for i in range(oblast_raboty[0],oblast_raboty[1] + 1):
    otvet += spisok_chisel[i]
print(otvet)
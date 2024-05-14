slova = []
kol_slov = int(input())
for i in range(kol_slov):
    slova.append(input())
for i in range(kol_slov):
    for j in range(i+1,kol_slov):
        if len(slova[i]) > len(slova[j]):
            slova[i], slova[j] = slova[j], slova[i]
        if len(slova[i]) == len(slova[j]):
            slova[i], slova[j] = slova[j], slova[i]
print(*slova, sep="\n")
kol_sat = int(input())
fam = set()
fam1 = set()
odinak = 0
for i in range(kol_sat):
    name = input()
    if not name in fam:
        fam.add(name)
        fam1.add(name)
    elif name in fam1:
        odinak += 2
        fam1.discard(name)
    else:
        odinak +=1
print(odinak)
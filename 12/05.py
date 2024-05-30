kod_isprav = []
for i in range(int(input()[1:])):
    kod = input()
    if '#' in kod.split():
        f = kod.index('#')
        kod = ''.join(kod[:f])
    kod_isprav.append(kod)
for i in range(len(kod_isprav)):
    print(kod_isprav[i])
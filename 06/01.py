my_set1 = set()
my_set2 = set()
while True:
    chislo = input()
    if chislo:
        my_set1.add(int(chislo))
    else:
        break
while True:
    chislo = input()
    if chislo:
        my_set2.add(int(chislo))
    else:
        break
my_set3 = my_set1 & my_set2
if not my_set3:
    print("EMPTY")
else:
    print(my_set3)



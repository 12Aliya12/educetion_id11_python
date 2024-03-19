kol_English = int(input())
kol_German = int(input())
kol_French = int(input())
my_set1 = set()
my_set2 = set()
my_set3 = set()
for i in range(kol_English + kol_German + kol_French):
    name = input()
    if name in my_set1:
        my_set2.add(name)
    elif name in my_set2:
        my_set3.add(name)
    else: my_set1




kol_english = int(input())
kol_german = int(input())
my_set1 = set()
my_set2 = set()
for i in range(kol_english):
    my_set1.add(input())
for i in range(kol_german):
    my_set2.add(input())
obsh = my_set1 ^ my_set2
if obsh:
    print(len(obsh))

else:
    print("NO")
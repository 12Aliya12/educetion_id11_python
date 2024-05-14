stroki = list()
konechnaya_stroki = list()
for i in range(int(input())):
    stroki.append(input())
kol_string_vivod = int(input())
for k in range(kol_string_vivod):
    poziciya = int(input())
    konechnaya_stroki.append(stroki[poziciya-1])
print(*konechnaya_stroki, sep="\n")
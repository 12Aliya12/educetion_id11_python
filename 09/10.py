spisok_chisel = list()
for i in range(int(input())):
    spisok_chisel.append(input())
spisok_diapozona = list()
nachalo_dapozona = int(input())
konec_diapozona = int(input())
spisok_diapozona.extend(spisok_chisel[nachalo_dapozona - 1:konec_diapozona])
s = 0
for k in spisok_diapozona:
    s = s + int(k)
print(s)
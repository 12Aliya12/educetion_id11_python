col_chisla = []
for i in range(int(input())):
    col_chisla.append(input())
proizvedenie_chisel = int(input())

for i in col_chisla:
    flagok = True
    for j in col_chisla:
       if i != j and int(i) * int(j) != int(proizvedenie_chisel):
           flagok = False
           break
if flagok:
    print("ДА")
else:
    print("НЕТ")
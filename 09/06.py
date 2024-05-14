spisok_chisel = list()
for i in range(int(input())):
    spisok_chisel.append(int(input()))
for k in range(len(spisok_chisel) - 1):
    print(spisok_chisel[k] + spisok_chisel[k+1])
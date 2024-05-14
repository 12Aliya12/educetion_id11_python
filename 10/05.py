soldats = []
for i in range(int(input())):
    soldats.append(input())
naryad_ocherednost = int(input())
for i in range(int(input())):
        del soldats [naryad_ocherednost - 1::naryad_ocherednost]
print(*soldats, sep="\n" )
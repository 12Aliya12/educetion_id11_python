alf_sahmat = "ABCDEFGH"
namber_kletki = int(input())
a = []
if namber_kletki < 9:
    a = [[k + 1 for k in range(8)] for i in range(8)]
for i in range(namber_kletki):
    for k in range(namber_kletki):
        print(alf_sahmat[k] + str(a[i][k]), end=' ')
    print()
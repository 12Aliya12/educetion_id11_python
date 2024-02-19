a1 = input()
a2 = input()
a3 = input()
if a1 > a2 and a1 > a3:
    if a2 > a3:
        print(a1, a2, a3)
    else:
        print(a1, a3, a2)
elif a2>a1 and a2 > a3:
    if a1 > a3:
        print(a2, a1, a3)
    else:
        print(a2, a3, a1)
elif a3 >a1 and a3>a2 :
    if a1>a2 :
        print(a3,a1,a2)
    else : print(a3, a2,a1)


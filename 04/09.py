simvol = int(input("Введите число: "))
stars = 1
probel = 10
while simvol > 0:
    print(" " * probel,  "*" * stars)
    probel -= 1
    stars += 2
    simvol -= 1

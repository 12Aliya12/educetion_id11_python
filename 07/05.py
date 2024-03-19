city = input()
while True:
    city1 = input()
    if city[-1] == city1[0]:
        city = city1
    else:
        print(city1)
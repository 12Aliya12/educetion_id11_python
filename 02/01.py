city1 = input()
city2 = input()
if city1 == "Тула" and city2 != "Пенза" and city2 != "Тула":
    print("ДА")
elif city1 != "Тула" and city2 == "Пенза" and city1 != "Пенза":
    print("ДА")
else:
    print("НЕТ")

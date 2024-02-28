people = int(input("Количество человек: "))
iq_people = 0
sum = 0
for i in range(1, people + 1):
    iq = int(input("Введите количество айкью: "))
    sredn = (iq + sum)/ i
    sum += iq
    if iq == sredn:
        print("0")
    elif iq > sredn:
        print(">")
    elif iq < sredn:
        print("<")
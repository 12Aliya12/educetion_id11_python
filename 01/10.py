print(" Вы находитесь в пещере на развилке. Вы можете пойти 'налево', 'направо' или 'прямо'" )
a1 = input()
if a1 == 'налево':
    print('Вы направились налево. Через некоторое время вы дошли до двух дверей. Вы выберете "левую" или "правую"?')
    a2 = input()
    if a2== 'правую':
         print("Вы смело открыли правую дверь. Но за ней вас подстерегала гигантская подземная жаба, которая проглотила вас целиком")
    else:
         print("Вы прошли игру!")
elif a1 == 'направо':
    print('Вы направились направо. Через некоторое время вы дошли до двух дверей. Вы выберете "левую" или "правую"?')
    a2 = input()
    if a2 == 'правую':
        print(
            "Вы смело открыли правую дверь. Но за ней вас подстерегала гигантская подземная жаба, которая проглотила вас целиком")
    else:
        print("Вы прошли игру!")
elif a1 == 'прямо':
    print('Вы направились прямо. Через некоторое время вы дошли до двух дверей. Вы выберете "левую" или "правую"?')
    a2 = input()
    if a2 == 'правую':
        print(
            "Вы смело открыли правую дверь. Но за ней вас подстерегала гигантская подземная жаба, которая проглотила вас целиком")
    else:
        print("Вы прошли игру!")
else:
    print("Вы указали не конкретный ход")
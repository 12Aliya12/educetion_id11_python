def space_game(text):
    kol_probel = 0
    for i in text:
        if i == " ":
            kol_probel += 1
    if kol_probel % 2 == 0:
        print("Вы выиграли")
    else:
        print("Вы проиграли")


s = input()
space_game(s)
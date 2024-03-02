stroka = int(input("Введите строку: "))
nach = False
for i in range(stroka):
    text = input("Введите текст: ")
    if ("кот" or "Кот") in text:
        nach = True
        if ("Пёс" or "пёс") in text:
            nach = False
if nach == True:
    print("МЯУ")
else:
    print("НЕТ")


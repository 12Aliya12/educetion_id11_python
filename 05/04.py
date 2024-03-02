stroka = int(input("Введите строку: "))
nach = False
for i in range(stroka - 1):
    text = input("Введите текст: ")
    if ("кот" or "Кот") in text:
        nach = True
        break
        text = input("Введите текст: ")
if nach == True:
    print("МЯУ")
else:
    print("НЕТ")
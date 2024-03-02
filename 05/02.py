stroka = int(input("Введите строку: "))
nach = False
for i in range(stroka - 1):
    text = input("Введите текст: ")
    if ("кот" or "Кот") in text:
        text = input("Введите текст: ")
        nach = True
if nach == True:
    print("МЯУ")
else:
    print("НЕТ")
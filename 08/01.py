slovo = input("Введите слово: ")
long_slovo = ''
short_slovo = ''
while slovo != "стоп":
    if len(slovo) > len(long_slovo):
        long_slovo = slovo
    if len(slovo) < len(short_slovo) or not short_slovo:
        short_slovo = slovo
    slovo = input("Введите слово: ")
funded = True
for text in short_slovo:
    if text not in long_slovo:
        funded = False
        break
if funded:
    print("ДА")
else:
    print("НЕТ")
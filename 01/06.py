print("Любите ли вы котиков?")
word1 = input()
print("Умеете ли вы программировать?")
word2 = input()

if word1 == "да" and word2== "да":
     print("Молодец")
elif word1 == "да" and word2 == "нет":
    print("Ну хорошо")
elif word1 == "нет" and word2 == "да":
    print("Ну нормально")
elif word1 == "нет" and word2 == "нет":
    print("Плохо")
else:
    print("Ошибка")


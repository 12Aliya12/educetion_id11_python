def parrot(phrase):
    if phrase in list_words:
        print(phrase)
    else:
        list_words.append(phrase)

list_words = list()
parrot("Привет")
parrot("Как тебя зовут?")
parrot("Привет")
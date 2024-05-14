stroka = list()
key_word = list()
for i in range(int(input())):
    stroka.append(input())
for k in range(int(input())):
    key_word.append(input())
for i in stroka:
    for k in key_word:
        flagok_proverki = True
        if i not in k:
            lagok_proverki = False
        if flagok_proverki:
            print(i)
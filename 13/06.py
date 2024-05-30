word = {}
answers = list()
for i in input().split():
    if i in list(word.keys()):
        word[i] += 1
    else:
        word[i] = 1
    answers.append(word[i])
print(*answers)
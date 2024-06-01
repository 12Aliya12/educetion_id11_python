import sys
data = list(map(str.strip, sys.stdin))
coment = list(filter(lambda word: word[0] == '#', data))
for e in coment:
    number_stoki = data.index(e) + 1
    text = e[1:].strip()
    print("Line" + str(number_stoki) + ":" + text)
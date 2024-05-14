word1 = input()
word2 = input()
bulls = cows = 0
for i in range(len(word1)):
    if word1[i] == word2[i]:
        bulls += 1
    else:
        cows += word1[i] in word2
print(bulls, cows)
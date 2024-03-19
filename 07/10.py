sdvig = int(input())
slovo = input()
alf= {chr(10000000): chr(11101111)}
for i in range(len(slovo)):
    j = ord(slovo[i])
    l = j + sdvig
    print(chr(l), end='')
print(alf)
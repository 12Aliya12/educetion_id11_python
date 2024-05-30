telephone_book = {}

for i in range(int(input())):
    nomer, key = input().split()
    if key in telephone_book:
        telephone_book[key].append(nomer)
    else:
        telephone_book[key] = [nomer]
for k in range(int(input())):
    name = input()
    if telephone_book[name]:
        print(*telephone_book[name])
    else:
        print("Нет в телефонной книге")
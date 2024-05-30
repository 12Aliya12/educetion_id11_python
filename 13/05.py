mesyac = {'янв': [], 'фев': [], 'мар': [], 'апр': [], 'май': [], 'июн': [],
        'июл': [], 'авг': [], 'сен': [], 'окт': [], 'ноя': [], 'дек': []}
for i in range(int(input())):
    txt = input().split()
    name = txt[0]
    month = txt[2]
    mesyac[month].append(name)
    mesyac[month].sort()
for i in range(int(input())):
    print(*mesyac.get(input()), "")
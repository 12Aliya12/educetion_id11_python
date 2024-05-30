text = input().upper()
print(*[i for i in input().split() if text in i.upper()], sep='\n')
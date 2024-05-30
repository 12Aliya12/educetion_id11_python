text = input().lower()
k = 0
for i in text:
    if text.count(i) > k:
        k = text.count(i)
print(k)
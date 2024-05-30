text = input().lower()
sorted_bukva = sorted(list(text.replace(" ", "")))
k = 0
max_pov = 0
for i in sorted_bukva:
    if text.count(i) > k:
        k = text.count(i)
        max_pov = i
print(max_pov)
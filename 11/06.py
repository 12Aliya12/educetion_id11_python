kol_product = int(input())
product = []
bez_luka= []
for i in range(kol_product):
    product.append(input())
for i in product:
    if "лук" not in i:
        bez_luka.append(i)
print(", ".join(bez_luka))
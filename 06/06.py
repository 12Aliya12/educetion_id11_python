kol_knig_bibl = int(input())
kol_knig_leto = int(input())
bibl = set()
leto = set()
for i in range(kol_knig_bibl):
    bibl.add(input())
for i in range(kol_knig_leto):
    leto.add(input())
for i in leto:
    intersection = bibl & leto
    if intersection:
        print("YES")
        leto = intersection - bibl
    else:
        print("NO")
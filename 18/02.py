def simple_map(transformation, values):
    spisok = []
    for i in values:
        spisok.append(transformation(i))
    return spisok


values = [1, 3, 1, 5, 7]
print(*simple_map(lambda x: x + 5, values))
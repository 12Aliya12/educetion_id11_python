marks = []
for num in range(int(input())):
    prom = []
    students_amount = int(input())
    for student in range(students_amount):
        part = input().split()
        prom.append(int(part[1]))
        if student == students_amount - 1:
            marks.append(prom)
if all([5 in item for item in marks]):
    print('Да')
else:
    print('Нет')
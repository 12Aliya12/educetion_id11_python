student_prohodnoy = []
all_student = []
for i in range(int(input())):
    student_s_ocenkami = input()
    student_s_ocenkami_spisok = student_s_ocenkami.split()
    if student_s_ocenkami_spisok[1] in ("4","5"):
        student_prohodnoy.append(student_s_ocenkami_spisok)
    all_student.append(student_s_ocenkami)
print(*all_student, sep="\n")
print("")
for one, two in student_prohodnoy:
    print(one, two)
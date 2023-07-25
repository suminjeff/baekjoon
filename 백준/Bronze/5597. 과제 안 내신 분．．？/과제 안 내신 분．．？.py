student_list = []

for i in range(1, 31):
    student_list.append(i)

for j in range(1, 29):
    student = int(input())
    student_list.remove(student)

for k in range(len(student_list)):
    print(student_list[k])

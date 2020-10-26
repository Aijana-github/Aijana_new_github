num = int(input("Введите кол-во студентов: "))
student_file = open('students.txt','w')
for i in range(num):
    student = input()
    student_file.write(student+' ')
student_file.close()
student_read = open('students.txt')
student_list = student_read.readlines()
for student in student_list:
    print(student)
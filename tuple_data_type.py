student1 =(1,'mg mg',22,'heldan')
student2 =(2,'su su',22,'heldan')
print(student1)

print("id=",student1[0])
print("name=",student1[1])
print("age=",student1[2])
print("address=",student1[3])


students = []
students.append(student1)
students.append(student2)

print(students)


my_student_array = [None, None, None]

my_student_array[1] = student1 
my_student_array[2] = student2

print(my_student_array)

print(my_student_array[1])
print(my_student_array[2])
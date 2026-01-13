from numpy import *

student = array('i',[88,99,90,87,90,98])
student_marks = array("i",[])
NO_student = int(input("No. of student"))

for i in range(NO_student):
    student_marks.append(int(input(f'enter marks for student {i+1} :- ')))
for i in range(NO_student):
    print(f"student no.{i+1} marks is :-",student_marks[i])
student.extend(student_marks)
a = len(student) 
for i in range(a):
    print(f"student no.{i+1} marks is :-",student[i])
for i in range (len(student)):
    print(f"student {i} marks {student[i]}")
j = 0
while(j <= ((len(student)))-1):
    print(f"student {j} marks {student[j]}")
    j+=1

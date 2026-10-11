question = '''1.	Three students have the following skills:
student_A = {"Python", "Java", "SQL", "HTML", "C"}
student_B = {"Python", "JavaScript", "SQL", "Java"}
student_C = {"Python", "C", "SQL", "MATLAB"}
Write a program to determine:
(a) Skills common to all three students.
(b) Skills known by exactly two students.
(c) Skills known by only one student.
(d) Total number of different skills known by the three students together.'''
student_A = {"Python", "Java", "SQL", "HTML", "C"}
student_B = {"Python", "JavaScript", "SQL", "Java"}
student_C = {"Python", "C", "SQL", "MATLAB"}
print("part a")
common_language = student_A.intersection(student_B,student_C)
print(common_language)
print("part b")
AB= student_A.intersection(student_B)-student_C
print("Course opted by only AB",AB)
BC = student_B&student_C - student_A
print("Course opted by only BC",BC)
AC = student_A&student_C - student_B
print("Course opted by only AC",AC)
print("Skills known for only two students are : ",AB|AC|BC)
print("part c")
A = student_A-(student_B|student_C)
print("Course only known by A is : ",A)
B = student_B-(student_A|student_C)
print("Course only known by B is : ",B)
C = student_C-(student_A|student_B)
print("Course only known by C is ",C)
print("Skills known by only one student are : ",A|B|C)
print("part d")
print("Total number of different skills known by the three students together are : ",student_A|student_B|student_C)
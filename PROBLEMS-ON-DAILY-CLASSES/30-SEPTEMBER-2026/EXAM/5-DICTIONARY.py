question = '''2.	Consider the following dictionary:
students = {
101: {"name": "Arun", "dept": "CSE", "marks": 87},
102: {"name": "Bala", "dept": "ECE", "marks": 92},
103: {"name": "Cathy", "dept": "CSE", "marks": 95},
104: {"name": "Divya", "dept": "ECE", "marks": 88},
105: {"name": "Esha", "dept": "CSE", "marks": 95},
106: {"name": "Farhan", "dept": "EEE", "marks": 91}
}


1	Print the name and marks of student 104.
2	Find the total marks of all students.
3	Print the roll number and name of every student in the ECE department.
4	Find the student with the lowest marks.
'''

students = {
101: {"name": "Arun", "dept": "CSE", "marks": 87},
102: {"name": "Bala", "dept": "ECE", "marks": 92},
103: {"name": "Cathy", "dept": "CSE", "marks": 95},
104: {"name": "Divya", "dept": "ECE", "marks": 88},
105: {"name": "Esha", "dept": "CSE", "marks": 95},
106: {"name": "Farhan", "dept": "EEE", "marks": 91}
}
print("part 1")
print(students[104]["name"],students[104]["marks"])
print("part 2")
sum =0 
for i in range(len(students)):
    sum +=students[i+101]["marks"]
print(sum)
print("part 3")
print("Roll numbers are : ")
for i in students.keys():
    print(i,end=" ")
print()    
print("part 4 ")    
lowest = 92
for i in students.keys():
    if students[i]["marks"]<lowest :
        lowest =students[i]["marks"]
print("Lowest is " ,lowest)       
   


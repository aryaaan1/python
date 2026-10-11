student_marks = {}  
student = int(input("Enter the number of student date you want to store : "))
for i in range(student):
#    we don't have to do thid loop beacuse before going on tqaht loop i need to add products
    # for j,k in student_marks.items():
        j = input("enter the name of the student")
        k = int(input("enter the marks of student"))
        student_marks[j] = k
print(student_marks)        
# average = 0        
# for i in student_marks.values():
#     average +=i        
# for i,j in student_marks.items() :
#     if j>average:
#         print(i)

       
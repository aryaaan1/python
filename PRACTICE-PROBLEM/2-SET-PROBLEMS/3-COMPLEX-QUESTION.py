Question2 = ''' A university stores each student's course registration as a tuple:
(student_id, student_name, department, (course1, course2, course3))
Write a Python program to:
•	Accept registration details for n students. 
•	Display students registered for a specified course.
•	Find the student registered for the maximum number of courses. 
•	Display the courses common to two selected students. 
•	Generate a tuple containing all unique courses offered'''



Regestration_Details = ()
n = int(input("Enter the number of the students : "))
print("Enter the details listed below : ")
for i in range(n):
    Student_id = int(input("Enter your student id : "))
    Student_name = input(" Enter your name : ")
    Department = input(" Enter the department you have been assigned : " )
    Course1 =input(" Enter the couse1 you have chosen : ")
    Course2 =input(" Enter the couse2 you have chosen : ")
    Course3 =input(" Enter the couse3 you have chosen : ")
    print(" Student_id Student_name Department Course1   Course2   Course3")

    Student_Course_Regestration = (f"{Student_id :<10}{Student_name :<14}{Department :<12}{Course1 :<9}{Course2:<11}{Course3:<11}")
    Regestration_Details +=(Student_Course_Regestration,)
    # comma is important for python to treat entire tuple as one element 
print(Regestration_Details)    
    
bool = True
while bool:
    Course = input("enter the course name : ")
    for j in Regestration_Details:
        pass

        


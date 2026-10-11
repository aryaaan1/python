marks = {"Arun":85,"Riya":92,"Rahul":78,"Anu":88,"Kiran":95,"Divya":82}
print("student names are :")
print(marks.keys())
print("Their marks respectively are : ")
print(marks.values())
a =0
for i in marks.values():
    if (i>a):
        a = i
print(a)        
b = max(marks.values())        
for i in marks.values() :
    if(i<b): 
        b =i     
print(b)         
        

sum =0 
n = len(marks)
for i in marks.values():
    sum +=i
   
average = sum/n
print(average)

score = 0
for i,j in marks.items():
    if(j>85):
        score +=1
        print("the student name is : ",i)

print("above are the  number of students got more than 85 are",score)        



count = 0
for i,j in marks.items():
    if(j>80):
        count +=1
        print("the student name is ",i)
print(" above are the number of people more than 80 are : ",count)        


    


    
    

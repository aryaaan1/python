from array import*
marks = array("i",[87,92,95,88,95,91])
sum = 0
for i in marks:
    sum = sum + i
print(sum)    
a = len(marks)
average = sum/a
print(average)



for i in range(len(marks)):
    print(marks[5-i],end = " ")
print()
for i in marks:
    if(i>90):
        print(i,end = " ")    

for i in range(len(marks)):
    if(marks[i] == 95):
        print("first ocuurence is",i)
        break
    
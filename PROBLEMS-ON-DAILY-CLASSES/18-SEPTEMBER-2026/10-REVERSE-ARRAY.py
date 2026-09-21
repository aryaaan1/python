import numpy as aryan

n = int(input("enter the number of elements : "))
a = []
for i in range(n):
    x = int(input("enter the number "))
    a.append(x)
    print(a)
d = aryan.array(a)

print(a,type(a))
print(d,type(d))    

import numpy as aryan

n = int(input("enter the number of elements : "))
a = []
for i in range(n):
    x = int(input("enter the number "))
    a.append(x)
    print(a)
d = sorted(a,key = lambda x:x[1])   
# d = aryan.array(a)
print(d)
print(a,type(a))
# print(d,type(d))    




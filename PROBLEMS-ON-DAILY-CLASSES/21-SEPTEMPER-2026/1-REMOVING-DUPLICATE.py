import numpy as aryan
a = aryan.array([10,50,30,20,30,10,60])
d =aryan.sort(a)
c = d.tolist()
print(c,type(c))
b = []
for i in c:
    if len(b)==0 or b[-1]!=i:
        b.append(i)
print(b)




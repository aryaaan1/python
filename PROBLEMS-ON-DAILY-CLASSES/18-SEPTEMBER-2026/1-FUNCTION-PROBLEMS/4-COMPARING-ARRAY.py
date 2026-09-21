import numpy as aryan
a = aryan.array([1,2,3])
b = aryan.array([3,2,3])
# it checks every value
print(a==b)
print(a>b)
c = a>b
print(aryan.any(c))
print(aryan.all(c))

d = aryan.array([1,2,0,-1,0,6])
print(aryan.where())
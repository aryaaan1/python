from array import*
a = array("i",[10,20,30,40,50])
print(a[1:4])
print(a[:])
print(a)
print(list(a))

for i in range(len(a)):
    print(a[i],end=" ")
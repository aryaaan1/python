depts = ("CSE","ECE","CSE","EEE","ECE","CSE")
count = 0
for i in depts:
    count = count +1
print("len of the depts is",count)   

h = list(depts)
h[3] = "MECH"
a = tuple(h)
print(a)
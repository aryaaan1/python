courseA =set(input("enter the names  in couseA: ").split(" "))
print(courseA)
courseB = set(input("enter the names in CourseB : ").split(" "))
print(courseB)
courseC = set(input("enter the names in course C : ").split(" "))
print(courseC)
# a = courseA.intersection(courseB,courseC)
# print(a)
# b = courseA-courseB-courseC
# c = courseB-courseA-courseC
# d = courseC-courseA-courseC
# e = b.union(c,d)
# print(e)

for i in courseA|courseB|courseC:
    count = 0
    if i in courseA:
        count +=1
    if i in courseB:
        count +=1
    if i in courseC:
        count +=1
    if count>=2:
        print(i,count)        




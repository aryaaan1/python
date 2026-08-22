marks = [12,13,14]
print(marks[0])

# append
fruits = ["mango","banana"]
fruits.append("litchi")
print(fruits)

# remove
fruits.remove("mango")
print(fruits)

# negative indexing(prints from back )
print(fruits[-1])

# change in element
fruits.append("melon")
fruits[0]="flower"
print(fruits)

# insert 
fruits.insert(2,"watermelon")
print(fruits)

# pop(removes from index
fruits.pop(1)
print(fruits)

# concatenation
a=[1,2,3]
b=[6,5,4]
print(a+b)

# repitation
c=[1,1,1,2]
print(c*3)

# lenght
print(len(c))

# count
print(c.count(1))

# position:index
print(fruits.index("flower"))

# maximum and minimum
print(max(1,2))
print(min(3,5))
# in list we can compare mutliple variable

# sum
print(max(a))
print(sum(a+b))


# sorting of list
b.sort()
print(b)

b.sort(reverse=True)
print(b)
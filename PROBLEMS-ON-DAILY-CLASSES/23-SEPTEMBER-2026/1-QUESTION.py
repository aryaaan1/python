x = {"1":1,"2":2,"3":4,"4":3}
sum = 0
a = 0
for i in x.values():
    sum +=i
    if(i>a):
        a = i


print(sum)
print(a)

# print(max(x.values()))

from array import*
a = array("i",[14,43,51,25,71,8,96,3,40,6])
d = list(a)
print(d)
d.sort()
print(d)

# n = int(input("enter the nth largest number you want to find :"))
# for i in range(a):
    # print(e[n+1])
print("the seventh largest number is",d[6])
print("the seventh smallest element is",d[-7])
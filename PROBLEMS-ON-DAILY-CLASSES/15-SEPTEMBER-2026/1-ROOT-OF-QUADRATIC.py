a = int(input("enter the value of a : "))
b = int(input(" enter the value of b : "))
c = int(input("enter  the vaule of c : "))
d = "a*(x**2)+b*x+c"
print(d)
print(f"{a}*(x**2)+{b}*x+{c}")
D = ((b**2)-4*a*c)**(1/2)
x1 = (1/2)*(-b + D)/a
x2 = (1/2)*(-b - D)/a
print(f"roots are {x1} and {x2}")
# if(D>0):
#     print("roots are positive")
# elif(D<0):
#     print(" roots are complex")    
# else:
#     print(" roots are eqaul") 
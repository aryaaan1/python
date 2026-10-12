n = int(input("enter the number : "))
a = []
for i in range(n):
  num = int(input("enter the number : "))
  a.append(num)

evenlist = []
oddlist =[]
for i in a:
  if(i%2 ==0):
    evenlist.append(i)
  else:
    oddlist.append(i)  
print("even list is " ,evenlist)   
print(" odd list is ",oddlist)
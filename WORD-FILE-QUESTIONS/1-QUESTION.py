QUESTION = '''	Python program to print all Prime numbers in an Interval '''
n = int(input("enter the interval : "))
for i in range(1,n):
    count = 0
    for j in range(2,i):
        if(i%j ==0):
           count +=1
           continue

      



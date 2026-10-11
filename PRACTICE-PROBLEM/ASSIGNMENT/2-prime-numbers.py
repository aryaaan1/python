start = int(input("from where you want to start : "))
end =  int(input("enter the last value : "))
for i in range(start,end+1):
    count = 0
    for j in range(2,i):
        if(i%j==0):
            count = 1
    if(count == 0 and i>=2)    :
        print(i)    
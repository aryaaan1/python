n = int(input("ENTER THE NUMBER : "))
reverse = 0
while(n>0):
    b = n%10
    reverse = reverse*10 + b
    n = n//10
print("THE REVERSE NUMBER IS :",reverse)    
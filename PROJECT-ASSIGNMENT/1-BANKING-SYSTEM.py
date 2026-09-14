balance = 0
while True:
    print(" 1- Deposit")
    print(" 2- Withdrawl")
    print(" 3- balance")
    print(" 4- Exit")
    choice =int(input ("enter your choice: ")) 

    if choice  == 1:
        amount = float (input(" enter the amount to deposit : "))

        if (amount>0):
            balance +=amount 
            print(" amount deposited sucessfully")
            print(" Current balanace ", balance)
        else:
            print(" please enter the valid amount ")

    elif choice == 2 :
        amount = float(input(" enter the amount to withdraw : "))   

        if amount<=0:
            print(" enter a valid number ")   
        elif amount>balance:
            print(" insuffcient balance ")
        else :
            balance -=amount
            print(" withdrawl successful")
            print("current balance ", balance)

    elif choice == 3 :
        if(balance>0):
          print(" your current balance is : ", balance)

    elif choice == 4:
        print(" thankyou for using our bank ")
        break

    else:
        print(" invalid choice please try again")    
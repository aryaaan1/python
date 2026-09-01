a = str(input("enter the string "))
count = 0
for z in a:
    if(z =='a'or z=='e' or z=='o' or z=='i' or z=='u'):
        print(z)
        count +=1
# if(count ==1)   :
#       print(" vowel is present")      
# elif(count ==0):
#   print(" no vowel is present")   
   
if(count ==0)   :
      print(" vowel is not present")      
else:
  print(" vowel is present")   
      
        
print("no of times it is present is " ,count)    
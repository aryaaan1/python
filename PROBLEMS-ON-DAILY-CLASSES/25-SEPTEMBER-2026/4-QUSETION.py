test1 = {"Aryan":21,"Harsh":49,"Ankit":50,"Alok":33}
test2 = {"Aryan" : 20,"Harsh" : 50,"Sunday":6,"Alok":40}
n = len(test1)
f= {}
for i,j in test1.items():
    for p,q in test2.items():
        if(i==p):
            sum = j + q
            print(f"marks of the {i} is {sum}")  
            f[i] = sum
print(f)            
                     

     
        

    

    
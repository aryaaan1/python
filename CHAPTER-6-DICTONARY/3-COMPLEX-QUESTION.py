employee = [("E101",45000,4.2,38),("E102",62000,3.8,42),("E103",38000,4.7,35),("E104",75000,3.5,45),("E105",52000,4.5,40)]
for i in employee:
    if(i[1]>60000 or i[2]<4.0):
        print(i[0],i[1],i[2])
list_of_employee = []
for i in employee:
    if(i[3]>40):
        list_of_employee.append(i[0])   
print(f"The employee who are working more than 40 hours are : {list_of_employee}") 
a=0 
b = 0
for i in employee:
    if(i[2]>a):
        a = i[2]
        b = i[0]
        
print(f"The employee who has most rating is : {b}  {a}")

# sales_amount = []
# for i in employee:
#     sales_amount.append(i[1])
# print(sales_amount)

# for i in range(len(sales_amount)):
#     for j in range(i+1,len(sales_amount)):
#         if(sales_amount[i]>sales_amount[j]):
#             sales_amount[i],sales_amount[j] = sales_amount[j],sales_amount[i]
# print(sales_amount)
print("Employee Details according to there salary Lowest to Highest : ")        
for i in range(len(employee)):
    for j in range(i+1,len(employee)):
        if(employee[i][1]>employee[j][1]):
            employee[i],employee[j] = employee[j],employee[i]
print(employee)  
sorted(employee,key=lambda x :x[1])
print(employee)











   
   
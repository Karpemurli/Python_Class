# 16.  Write a program to accept the cost price of a bike and display the road tax to be paid according to the following criteria :
    
#         Cost price (in Rs)                                    Tax
#         > 100000                                                  15 %
#         > 50000 and <= 100000                            10%
#         <= 50000                                                   5%


Cost_prise=int(input("Enter the Bike cost Price:"))

if Cost_prise > 100000:
    tax= Cost_prise* 0.15
elif Cost_prise > 50000 and Cost_prise <= 100000:
    tax=Cost_prise* 0.10
else:
    tax=Cost_prise* 0.5


print("Road Tax to be Paid:",tax)
    
    
    
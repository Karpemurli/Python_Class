# Write a python program to find factorial value entered by user
# 5 ===5 *4*3*2*1 ---> 120

numbers=int(input("Enter a number="))

factorial=1

if numbers < 0:
    print("negative numbers")
else:
    for i in range(1, numbers+1):
        factorial *= i
    print("factorial Number: ",factorial)
    
    


    




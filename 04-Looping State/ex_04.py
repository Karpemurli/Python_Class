# Write a python program to find factorial value entered by user
# 5 ===5 *4*3*2*1 ---> 120




num=int(input("enter the num=="))
factorial=1

i=1

while i < num+1:
    factorial=factorial*i
    print(i)
    i+=1
print("factorial=", factorial)

# num=int(input("Enter a number="))
# factorial=1

# for i in range(1, num+1):
#     factorial = factorial*i
# print("factorial number=",factorial)


# using while loop
# i=1
# while i<num:
#     factorial *= i
#     i += 1

# print("factorial number=",factorial)






# numbers=int(input("Enter a number="))

# factorial=1

# if numbers < 0:
#     print("negative numbers")
# else:
#     for i in range(1, numbers+1):
#         factorial *= i
#     print("factorial Number: ",factorial)
    
    


    




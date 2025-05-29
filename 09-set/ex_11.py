#  Write a Python program to find the two numbers whose product is maximum among all the pairs in a given list of numbers. Use the Python set.
# 1,3,-10,7,-20,9,1
numbers = [-30,12,-5,11,4,-10]

unique_numbers = set(numbers)
sorted_numbers = sorted(unique_numbers)

#[-20, -10, 1, 3, 7, 9]

#find largest two numbers
largest1 = sorted_numbers[-1]
largest2 = sorted_numbers[-2]

#find smallest element
smallest1 = sorted_numbers[0]
smallest2 = sorted_numbers[1]

#calculate the product
prod1 = largest1 * largest2
prod2 = smallest1 * smallest2
if prod1 > prod2:
    print("The two number with largest prodcut is",largest2,"and",largest1)
    print("The product is = ",prod1)
else:
    print("The two number with largest prodcut is",smallest2,"and",smallest1)
    print("The product is = ",prod2)
    
    
    
    
# set1=set([-30,12,-5,11,4,-10])

# unique_num=set(set1)

# sorted_num=sorted(unique_num)



# #find two largest numbers

# largest1=sorted_num[-1]
# largest2=sorted_num[-2]

# #find smallest number

# smallest1=sorted_num[0]
# smallest2=sorted_num[1]

# #calculate the product

# prod1=largest1*largest2
# prod2=smallest1*smallest2

# if prod1 > prod2:
#     print("The two numbers with largest product is",largest2,"and",largest1)
#     print("the product is:",prod1)
# else:
#     print("The two numbers with largest product is",smallest2,"and",smallest1)
#     print("the product is:",prod2)





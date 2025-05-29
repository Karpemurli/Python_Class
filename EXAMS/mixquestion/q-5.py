# Write a Python program to count the number of vowels in a given string.

# def vovels_con(s):
    
#     vovels="aeiouAEIOU"

#     count=0
    
#     for i in s:
#         if i in vovels:
#             count+=1
    
    
#     return count

# s=input("Enter a string: ")

# print("Number of vowels: ",vovels_con(s))



def vovels(s):
    
    vovels="aioueAIOUE"
    
    
    count=0
    
    
    for char in s:
        if char in vovels:
            count+=1
        
        
    return count

s=input("Enter a string:")

print("Number of vowels: ",vovels(s))
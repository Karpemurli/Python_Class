
# 4. Write a Python program that executes a list operation and handles an AttributeError exception if the attribute does not exist.

# new=int(input("enter a num:"))
# lst=[1,2,3,4,5,6,7,8,9,10]

# lst.append(new)

# print(lst)


try:
    new=int(input("enter a num:"))
    lst=[1,2,3,4,5,6,7,8,9,10]
    lst.append(new)
    print(lst)
except AttributeError as e:
    print("An AttributeError occurred:",e)
except Exception as e:
    print("An unexpected error occurred:",e)
    
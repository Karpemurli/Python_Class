# Write a program to find whether a given number is a prime number or not using conditional statements and loops.


# num=int(input('Enter A number:'))

# if num > 1:
#     for i in range(2,num):
#         if (num % i == 0):
#             print(f"{num} is a not a prime number")
#             break
#     else:
#         print(f"{num} is a prime number")
        
# else:
#     print(f"{num } is not a prime number")


# Prime Number Check Using Recursion


def is_prime(num,divisor=None):
    
    if num < 2:
        return False
    
    
    if divisor is None:
        divisor= num - 1
        
    if divisor == 1:
        return True
    if num % divisor == 0:
        return False
    
    
    return is_prime(num,divisor - 1)

num=int(input("enter the number:"))

if is_prime(num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")
    
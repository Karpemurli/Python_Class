
# # # 42.	Write a Python program to find the factorial of a number using loops.


num=int(input('Enter a nm = '))


fact=1

i=1


while i <= num:
    fact=fact*i
    print(i)
    i+=1
    
print(f'factorial= ',fact)


    
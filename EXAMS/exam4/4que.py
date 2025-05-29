# 4)	Write a program to enter any digit number and print its reverse

num=int(input("Enter a digit number="))


revesed=0

while num != 0:
    digit=num % 10
    revesed=revesed*10+digit
    num //= 10
    
print("Reversed number=", revesed)
    
    



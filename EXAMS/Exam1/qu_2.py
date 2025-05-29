##Write a program to check whether it is palindrome number or not.




num= input('Enter a number=')

reversed = num[::-1]


# print(reversed)


if num == reversed:
    print(num,'is a palindrome number')
else:
    print(num,'is not a palindrome number')


# num=[0,1,2,3,4,5,6,7]

# print(num[1])
# print(num[::-1])



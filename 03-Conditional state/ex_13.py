##Write a program to check whether it is palindrome number or not.

# ans=A palindrome number is a number that reads the same forward and backward.
num= input('Enter a number=')

reversed = num[::-1]


if num == reversed:
    print(num,'is a palindrome number')
else:
    print(num,'is not a palindrome number')




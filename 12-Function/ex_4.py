# Exercise 4: Define a function that accepts a number and returns whether the number is even or odd.



def number(num):
    if num % 2 == 0:
        return 'even'
    else:
        return 'odd'


num = int(input('Enter a number:'))
statament=number(num)

print(f'{num} is {statament}')
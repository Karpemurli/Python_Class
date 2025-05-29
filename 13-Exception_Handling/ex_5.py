# Exercise 3: Define a function in python that accepts 3 values and returns the maximum of three numbers.


def maximum(a,b,c):
    try:
        if a >= b and a >= c:
            return a
        elif b >= a and b >= c:
            return b
        else:
            return c
    except Exception as m:
        return str(m)
try:
    a=int(input('Enter A Number:'))
    b=int(input('Enter A Number:'))
    c=int(input('Enter A Number:'))
    
    maxi=maximum(a,b,c)
    print('\nMaximum Number:',maxi)
except Exception as d:
    print(d)

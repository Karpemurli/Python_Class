# Exercise 4: Define a function that accepts a number and returns whether the number is even or odd.





def check_number(Num):
    try:
       
        
        if Num % 2 == 0:
            return 'Even'
        else:
            return 'Odd'
    except Exception as e:
        return str(e)
    
try:
    Num=int(input('Enter A Number:'))
    re=check_number(Num)
    print(f"{Num} is {re}.")
except Exception as r:
    print(r)
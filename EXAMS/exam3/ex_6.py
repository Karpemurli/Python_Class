# 6. Write a function that returns the first n numbers in the Fibonacci sequence. Example: fibonacci(5) → [0, 1, 1, 2, 3].


def fibonacci(number):
    
    if number <= 0:
        return []
    elif number == 1:
        return[0]
    
    seq=[0,1]
    for _ in range(2,number):
        seq.append(seq[-1]+seq[-2])
    return seq
        
    
    
number=int(input('Enter the number:'))

ans=fibonacci(number)

print(ans,end=" ")
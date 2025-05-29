# 5.	How can you find the second largest number in a list without using sorting?


def second_nm(lst):
    
    first=0
    second=0
    
    for i in lst:
        if i > first:
            second=first
            first=i
            
        elif second < i < first:
            second=i
            
    return second

lst=[10,55,44,66,88,10,101]

Second_largest=second_nm(lst)

print("Second largest number is:",Second_largest)
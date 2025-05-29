# 41.	How do you check if a string is a palindrome using loops and conditional statements?



def palindrome(s):
    
    s=s.lower()

    left=0
    right=len(s)-1
    
    
    while left < right:
        if s[left] != s[right]:
            return False
        
        
        left +=1
        right-=1
        
    return True

in_str=input("Enter a string:")

if palindrome(in_str):
    print(f"{in_str} is a palindrome")
else:
    print(f"{in_str} is not a palindrome")



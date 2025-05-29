
# 44.	How do you reverse a string in Python using loops?


# def revered(s):
    
    
#     rev=""
    
#     for i in s:
#         rev=i+rev
        
#     return rev

# demo=input("enter string = ")

# print(revered(demo))

#______________________________________________________________


# def reversed(s):
    
#     re_str=""
#     i=len(s)-1
    
#     while i >= 0:
#         re_str +=s[i]
        
#         i-=1
#     return re_str

# s="Hello World!"
# print(reversed(s))



def reversed(s):
    
    
    re_str=""
    i=len(s)-1
    
    
    while i >= 0:
        re_str +=s[i]
        
        i-=1
    return re_str

demo=input('enter string=')

print(reversed(demo))




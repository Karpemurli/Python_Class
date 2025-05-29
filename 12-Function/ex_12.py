# Write a Python function that accepts a string and counts the number of upper and lower case letters.
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12


def demo(letters):
    uppercase=0
    lowercase=0
    
    for i in letters:
        if i.isupper():
            uppercase+=1
        elif i.islower():
            lowercase+=1
    
    if uppercase > 0 and lowercase > 0:
        print("No. of Upper case characters :",uppercase)
        print("No. of Lower case characters :",lowercase)
    else:
        print("No uppercase or lowercase letters found.")
            
    
   


letters=str(input("Enter Sample Strings:"))

demo(letters)
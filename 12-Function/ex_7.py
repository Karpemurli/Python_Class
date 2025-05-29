
# Exercise 7: Define a function that accepts lowercase words and returns uppercase words.



def murali(word):
    if word != word.upper():
        wo=word.upper()
        print('The word in Uppercase is:',wo)
        return wo
    else:
        print('The word is already Uppercase.')
        return word
    
word=str(input('Enter a word:'))

murali(word)
murali(word)

#swapcase=convert upper to lowercase
#                  lower to upper 

# def swapnil(wo):
#     if wo != wo.swapcase():
#         sw=wo.swapcase()
#         print("The word is:",sw)
#         return sw
#     else:
#         print("invalid word:",wo)
#         return wo

# wo=str(input('Enter a word:'))

# swapnil(wo)
             


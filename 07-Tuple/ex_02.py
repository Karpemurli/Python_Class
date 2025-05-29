# Write a Python program to remove punctuation from a given string.
# Sample Output:
# Original text:
# String! With. Punctuation?
# After removing Punctuations from the said string:
# String With Punctuation

text='String! With. Punctuation?'
punctuation="!.?"

new_text=""
for i in text:
    if i not in punctuation:
        new_text += i
        
print(new_text)

# print("Original text:")
# print(text)

# punctuation="!.?"

# new_text=""

# for i in text:
#     if i not in punctuation:
#         new_text+=i

# print("After removing Punctuations from the said string:")
# print(new_text)





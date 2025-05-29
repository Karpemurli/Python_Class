# Exercise 5: Define a function which counts vowels and consonant in a word.




def words(word):
    vowels='aeiouAEIOU'
    vo=0
    co=0
    for char in word:
        if char.isalpha():
            if char in vowels:
                vo+=1
            else:
                co+=1
    return vo,co

word=input('Enter a word:')

vo,co=words(word)

print(f"vowels :{vo}, consonant: {co}")
     
# Exercise 5: Define a function which counts vowels and consonant in a word.

def count(words):
    try:
        vowels='aeiouAEIOU'
        vo=0
        co=0
        for char in words:
            if char in vowels:
                vo+=1
            else:
                co+=1
        return vo,co
    except Exception as d:
        return str(d)


try:
    words=input("Enter the words=")
    vo,co=count(words)
    print(f"vowel={vo} conson={co}.")
except Exception as e:
    print(e)




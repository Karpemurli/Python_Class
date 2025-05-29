
# 7. Develop a function to check if two strings are anagrams. Example: is_anagram("listen", "silent") → True.

import random
def random_name():
    first_name=["Murali","Raj","swapnil","Harsh","Omkar","Rohan","Nayan","Bhushan"]
    last_name=["patil","Mali","Karape","Koshti","mahadik","dandvate","deshmukha"]
    
    first_name=random.choice(first_name)
    Last_name=random.choice(last_name)
    
    full_name=f"{first_name} {Last_name}"
    
    return full_name

name=random_name()
print(f"Randomly name:{name}")
    
    
    


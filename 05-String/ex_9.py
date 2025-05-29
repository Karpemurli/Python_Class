# index method using update

mystring = input("Enter the string: ")

demo = input("Word to update: ")
demo2 = input("New word: ")

# Check if the word exists in the string
if demo in mystring:
    # Replace the word using the replace() method
    mystring = mystring.replace(demo, demo2, 1)  # Replaces only the first occurrence
    print("Updated string:", mystring)
else:
    print(f"Word '{demo}' not found in the string.")

    
    
    



    
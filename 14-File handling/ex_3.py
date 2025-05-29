# 1. Write a Python program to read a file line by line store it into a variable.


try:
    with open(r'D:\python\14-File handling\text1.txt','r') as f:
        lines= f.readlines()
        
    for i in lines:
        print(i.strip())

except FileNotFoundError:
    print("check file not found..")
    
except Exception as e:
    print(f"An error occurred: {e}")
        


# try:
#     # Specify the file path
#     file_path = r"D:\python\14-File handling\text1.txt"
    
#     # Read the file line by line and store it in a variable
#     with open(file_path, "r") as file:
#         lines = file.readlines()  # Reads all lines into a list
    
#     # Print the variable to verify its content
#     for line in lines:
#         print(line.strip())  # Strip removes extra newline characters while printing
# except FileNotFoundError:
#     print("File not found")


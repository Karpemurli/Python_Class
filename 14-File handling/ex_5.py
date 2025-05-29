# 2# 3. Write a Python program to count the number of lines in a text file.








# try:
#     filepath=r'D:\python\14-File handling\text.txt'
    
#     with open(filepath,'r') as file:
#         numoflines=0
#         for i in file:
#             numoflines+=1
#         print(f"Number of lines={numoflines}")
# except FileNotFoundError:
#     print("File not found")
# except Exception as e:
#     print(f"An error occurred: {e}")

try:
    fp=r'D:\python\14-File handling\text1.txt'
    with open(fp,'r')as d:
        numoflines=0
        for i in d:
            numoflines+=1
        print(f'Number all lines={numoflines}')
except FileNotFoundError:
    print('File not found')
    

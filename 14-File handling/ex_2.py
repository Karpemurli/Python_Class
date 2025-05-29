

# 2. Write a Python program to append text to a file and display the text.

# with open('D:\\python\\14-File handling\\text1.txt',"a") as fp:
#     fp.write("\tThis is a new line in the file.")
    
    
try:
    #append text to file
    with open(r'D:\python\14-File handling\text1.txt',"a") as fp:
        fp.write("\n strenger thinge.")
      
      #read the file
    with open(r'D:\python\14-File handling\text1.txt',"r") as filep:
        print(filep.read())
        fp.close()
except FileNotFoundError:
    print("File not found")
    

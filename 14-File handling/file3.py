


# Q. How we can take user input to create a file?
import os



file_path=r"D:/python/14-File handling/"


file_name=input("Enter the name of the file=")

compile_path=file_path+" "+file_name
print("The path is=",compile_path)
if os.path.exists(compile_path):
    print("File already exists...")
else:
    with open(compile_path,"a") as fp:
        fp.write("file contents are stored.")


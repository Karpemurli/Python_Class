
# Q. How we can check if file exist at given location.


# import os

# file_path=r"D:\python\14-File handling\text1.txt"

# if os.path.exists(file_path):
#     print("File exists")
    
# else:
#     with open(file_path,"w") as fp:
#         fp.write("This is a new file")

import os


fp=r"D:\python\14-File handling\txt1.txt"


if os.path.exists(fp):
    print("File exists")
else:
    with open(fp,'w') as fp:
        fp.write("This is a new file")
        
        
        
#file adhich save asel tr tyat data type honar nahi tr new file tayar honar.

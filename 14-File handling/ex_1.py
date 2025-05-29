# 1. Write a Python program to read an entire text file.





try:
    fp=open(r"D:\python\14-File handling\text.txt", "r")
    print(fp.read())
    fp.close()
except FileNotFoundError:
    print("The file does not exist.")



# def read_file(file_path):
#     try:
#         with open(file_path, 'r') as file:  # Open the file in read mode
#             content = file.read()          # Read the entire file content
#         print(content)
#     except FileNotFoundError:
#         print(f"Error: The file '{file_path}' does not exist.")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# # Specify the path to your file
# file_path = r"D:\python\14-File handling\text.txt"

# read_file(file_path)



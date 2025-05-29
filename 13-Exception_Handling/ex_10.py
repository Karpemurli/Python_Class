# 3. Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.


def open_file():
    try:
        with open(r"E:\RESUME.pdf",'rb') as file:
            content=file.read()
            print(content[:100])
    except FileNotFoundError as e:
        print(f"The file does not exist: {e}")
    except Exception as e:
        print(f"error: {e}")


open_file()
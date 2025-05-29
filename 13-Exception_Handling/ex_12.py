
#2. Write a Python program that executes an operation on a list and handles an IndexError exception if the index is out of range.

# def numbers():
#     try:
#         num=[1,2,3,4,5]
#         print(num[10])
#     except IndexError as w:
#         print(str(w))
#     except Exception as e:
#         print(str(e))


# numbers()



def numbers():
    try:
        num=[1,2,3,4,5]
        print("Simple List:",num)
        
        index=int(input("Enter a number:"))
        
        ele=num[index]
        print("Element at index",index,":",ele)
        
      
    except IndexError as w:
        print(str(w))
    except Exception as e:
        print(str(e))

numbers()


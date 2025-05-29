#  1. Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical.



def main(nm1,nm2):
    try:
        nm1=input('Enter a Number=')
        nm2=input('Enter a Number=')
        
        
        nm1=int(nm1)
        nm2=int(nm2)
        
        print(f"First Number is={nm1} \nSecond Number is={nm2}")
        return nm1,nm2
    except ValueError as e:
        print(str(e))
    except Exception as e:
        print(str(e))
        
nm1,nm2=main(None,None)
        
        
        
        
    

    
          
   

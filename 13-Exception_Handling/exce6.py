


#custom exception

class myname(Exception):
    def __init__(self, message="Negative numbers are not allowed"):
        super().__init__(message)
        
     
def square_root(number):
    if number < 0:
            raise myname("Cannnot compute the square root of neagtive number")
    return number ** 0.5

try:
    result=square_root(36)
    print(result)
except myname as err:
    print(err)


    
    
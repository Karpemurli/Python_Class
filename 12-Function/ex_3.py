# Exercise 3: Define a function in python that accepts 3 values and returns the maximum of three numbers.



def num(x,y,z):
    if x >= y and x >=z:
        return x
    elif y >= x and y >= z:
        return y
    else:
        return z
    
  
        
    
   
    
    
x= int(input('enter the number:'))
y= int(input('enter the number:'))
z= int(input('enter the number:'))

maximun=num(x,y,z)

print("Maximun Number:",maximun)
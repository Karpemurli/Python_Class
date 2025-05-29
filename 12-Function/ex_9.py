#  Write a Python function to sum all the numbers in a list.



def main(numbers):
    total=0
    for i in numbers:
        total += i
    return total
        
        
    
    
numbers=[1,2,3,4,6]
print("The sum is:",main(numbers))

    
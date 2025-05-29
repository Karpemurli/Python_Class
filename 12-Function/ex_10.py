# Write a Python function to multiply all the numbers in a list.


def multiply_numbers(numbers):
   
    result = 1
    for num in numbers:
        result *= num
    return result

# Example usage:
numbers = [2, 3, 4, 5]
print("original list:",numbers)
print("multiply all:", multiply_numbers(numbers))


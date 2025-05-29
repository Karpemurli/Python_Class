# Exercise 2: Define a function that accepts roll number and returns whether the student is present or absent.

    
    
def presenty(present_num,Number):
    try:
        if Number in present_num:
            return 'Present'
        else:
            return 'Absent'
    except Exception as e:
        return str(e)

try:
    present_num=[1,2,3,4,5,6,7,8,9,10,11,12,13,]
    Number=int(input('Enter a number: '))
    
    status=presenty(present_num,Number)
    print(f"{Number} Number is {status}.")
except Exception as m:
    print(f"Error: {m}")
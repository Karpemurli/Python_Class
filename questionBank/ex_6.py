# 6. Write a program that prompts the user to input a number from 1 to 7. 
# The program should display the corresponding day for the given number. 
# For example, if the user types 1, the output should be Sunday. 
# If the user types 7, the output should be Saturday. 
# If the number is not between 1 to 7 user should get error message as shown in sample output.


def week():
    
    
    day=int(input('Enter the number of days:'))
    
    match day:
        
        case 1:
            print('sunday')
        case 2:
            print('Monday')
        case 3:
            print('Tuesday')
        case 4:
            print('Wednesday')
        case 5:
            print('Thursday')
        case 6:
            print('Friday')
        case 7:
            print('Saturday')
        case _:
            print(f'invalid number: {day}')        

week()

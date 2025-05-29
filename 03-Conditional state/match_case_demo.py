# Prompt user for input
week_days = int(input("Enter a week number: "))

# Match case to determine the day of the week
match week_days:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid number, please enter a number between 1 and 7.")

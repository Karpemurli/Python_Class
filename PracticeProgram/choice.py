

def Basic_Program():
    print("\nBasic Program:")
    print("1)Positive/Negative/Neutral")
    print("2)Even/Odd")
    print("3)Square")
    print("4)Cube")
    print("5)Exit")
    
def POSitive_Program(member):
    n=int(input("Enter the Number:"))
    if n > 0:
        print("positive")
    elif n < 0:
        print("negative")
    else:
        print("zero")


def odd_even(member):
    n=int(input("Enter the Number:"))
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")
def square(member):
    n=int(input("enter the Square:"))
    print("Square:",n*n)
def cube(member):
    n=int(input("enter the nmber:"))
    print("Cube is",n*n*n)

def main():
    member=()
    while True:
        Basic_Program()
        choice=int(input("\nEnter the Choice Number:"))
        if choice == 1:
            POSitive_Program(member)
        elif choice == 2:
            odd_even(member)
        elif choice == 3:
            square(member)
        elif choice == 4:
            cube(member)
        elif choice == 5:
            print("Exiting Program...")
            break
        else:
            print("Invalid Choice....")


if __name__ == "__main__":
    main()
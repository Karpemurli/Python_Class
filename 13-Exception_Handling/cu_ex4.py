# 5. Custom Exception for Invalid Grade


class Invalidgrade(Exception):
    def __init__(self, msg="Invalid grade !"):
        super().__init__(msg)
        
def validgrade(grade):
    validgrade={"A","B","C","D","E","F"}
    
    if grade.upper() not in validgrade:
        raise Invalidgrade(f"Invalid grade {grade}.")


def main():
    try:
        grade=input("Enter the grade=").strip()
        validgrade(grade)
        print(f"Grade is Valid: {grade}")
    except Invalidgrade as e:
        print(str(e))
    else:
        print("Program Ended")


if __name__ == "__main__":
    main()
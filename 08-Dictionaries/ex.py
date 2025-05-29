# Write a program to input roll numbers and their names of students of your class and
# store them in the dictionary as the key-value pair. Perform the following operations on
# the dictionary:
# a) Display the Roll numbers and name for all students.
# b) Add a new key-value pair in this dictionary and display the modified dictionary
#c) Delete a particular student's record from the dictionary
# d) Modify the name of an existing students.

def create_project():
    print("\n***Personal Information***")
    print("1) Display all information")
    print("2) Add new person=")
    print("3) Delete the person=")
    print("4) Modified the person=")
    print("5) Exite....")
    
def display_all_info(member):
    if member:
        print("\n All Student Details:")
        for name, details in member.items():
            print(f"Name:{name},Roll No:{details['Roll_num']},Class Name:{details['class_name']}")
    else:
        print("No Student Details....")
    
    
def add_person(member):
    while True:
        name=input('Enter name:').lower()
        Roll_num=input('Roll number:').lower()
        class_name=input('class name:').lower()
    
        member[name]={'Roll_num':Roll_num,'class_name':class_name}
    
        more=input('add other person (yes/no):').lower()
        if more != 'yes':
         break
    
def delete_person(member):
    name=input("Enter name:").lower()
    
    if name in member:
        print("\n delete the person.")
        print(f"Name:{name},Roll No:{member[name]['Roll_num']},Class Name:{member[name]['class_name']}")
        del member[name]
    else:
        print("Person not found.")
def edit_person(member):
    name=input("Enter name:").lower()
     
     
    if name in member:
        print('\nCurrent Details:')
        print(f"Name:{name},Roll No:{member[name]['Roll_num']},Class Name:{member[name]['class_name']}")
        
        Roll_num=input("Roll Number:").lower()
        class_name=input("Class Name:").lower()
         
        if Roll_num:
            member[name]['Roll_num'] = Roll_num
        if class_name:
            member[name]['class_name'] = class_name
             
        print('\n Details Updated.')
        print(f"Name:{name},Roll No:{member[name]['Roll_num']},Class Name:{member[name]['class_name']}")
    else:
        print("Person not found.")

def main():
    member={}
    
    while True:
        create_project()
        choice=input("Enter Your Choice:")
        
        if choice == '1':
            display_all_info(member)
        elif choice == '2':
            add_person(member)
        elif choice == '3':
            delete_person(member)
        elif choice == '4':
            edit_person(member)
        elif choice == '5':
            print("Exiting Program....")
            break
        else:
            print("Invalid Choice....")
if __name__ == "__main__":
    main()



         
         
    
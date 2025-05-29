# Create a simple project using python and List,
# 1. Add personal details 
# 2. Edit the details
# 3. Search particular person
# 4. delete the person

# - When I insert the data it will ask for me to add another data.

def create_project():
    print("\n***Personal Information***")
    print("1)Add personal information =")
    print("2) Search particular person =")
    print("3) Edit the person=")
    print("4) Delete the person=")
    print("5) Display all personal information")
    print("6) Exite....")
        
def add_person(member):
    while True:
        person={}
        person['name']=input("Enter Name:").lower()
        person['lname']=input('Enter LName:').lower()
        person['age']=input("Enter age:").lower()
        member.append(person)
        
        more=input("Ani Konachi Information Add karayachi ahe ka(yes/no):").lower()
        if more != "yes":
            break
        
def search_person(member):
    name=input("Enter Name:").lower()
    
    for person in member:
        if person['name'] == name:
            print("\nFound the Person....")
            print(person)
            return
        # else:
        #     print("\nNot Found....")
        # return
    print('person Not Found...')
    
def edit_person(member):
    name=input('Enter Name:').lower()
    
    for person in member:
        if person['name'].lower() == name.lower():
            print("\n cureent Details...")
            print(person)
            person['name']=input('Enter The New Name:')or person['name']
            person['lname']=input('Enter The New LName:')or person['lname']
            person['age']=input('Enter The New Age:')or person['age']
            print("\nDetails Updated...")
            print(person)
            return
    print('Person Not Found...')
    
    
def delete_person(member):
    name=input('Enter Name:')
    
    for person in member:
        if person['name'].lower() == name.lower():
            member.remove(person)
            print('\n delete the person')
            print(person)
            return
    print('Person Not Found...')
    
def display_all_person(member):
    if member:
        print('\n***All Memeber Details ***')
        for person in member:
            print(person)
            person+=1
    else:
        print('\nNo Memeber Details....')
            
    
    

            
            
def main():
    member=[]
     
    while True:
         create_project()
         choice=input("Enter your choice:")
         
         if choice == '1':
             add_person(member)
         elif choice == '2':
             search_person(member)
         elif choice == '3':
             edit_person(member)
         elif choice == '4':
             delete_person(member)
         elif choice == '5':
             display_all_person(member)
         elif choice == '6':
             print("Exiting Program....")
             break
         else:
             print("Invalid Choice....")
             
if __name__ =="__main__":
    main()
         
    

        
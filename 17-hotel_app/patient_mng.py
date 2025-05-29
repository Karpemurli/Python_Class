import pymysql as ss
from dotenv import load_dotenv
from tabulate import tabulate
import os
import pyautogui


load_dotenv()
my_password=os.getenv("db_pass")
# print(my_password)

def connect_db():
    return ss.connect(host='localhost',user='root',passwd=my_password,database='patientmng')

def commit_message(cursor,db,message):
    db.commit()
    print(message)
    
#________________________________________________________ login ______________________________________________

def login(cursor):
    uname=input('\n Enter the Username = ').strip()
    upass=pyautogui.password(text="Enter the user password :",title='Enter Password',default='',mask='*')
    
    
    cursor.execute('select * from login where uname=%s and upass=%s' ,(uname,upass))
    user=cursor.fetchone()
    
    if user:
        print('Login successfully')
        return True
    else:
        print('Invalid username and password please check again')
        
#___________________________________________________ Patient Management _______________________________________


def add_patients(cursor,db):
    while True:
        
        name=input('Enter the Patient Name = ').title().strip()
        age=int(input('Enter the patient age = '))
        gender=input('Enter the patient gender (Male/female/other) = ').title().strip()
        contact=input('Enter the Contact = ')
        
        cursor.execute('insert into patients (name,age,gender,contact) values(%s,%s,%s,%s)',(name,age,gender,contact))
        commit_message(cursor,db,'\nData Inserted Successfully')
        view_patients(cursor,db)
        
        
        result=input('Do you want to add another patient? (yes/no) = ').strip().lower()
        
        if result == 'no':
            break
    
def update_patients(cursor,db):
    patient_id=int(input('Enter the Patient ID = '))
    
    name=input('Enter the New Patient Name = ').title().strip()
    age=int(input('Enter the New patient age = '))
    gender=input('Enter the New patient gender (Male/female/other) = ').title().strip()
    contact=input('Enter the New Contact = ')
    
    cursor.execute('update patients set name=%s,age=%s,gender=%s,contact=%s where pid=%s',(name,age,gender,contact,patient_id))
    commit_message(cursor,db,'One record updated')
    
    cursor.execute('select * from patients where pid=%s',(patient_id,))
    result=cursor.fetchone()
    
    if result:
        columns=['Patients_ID',"Name","Age","Gender","Contact"]
        print(tabulate([result],headers=columns,tablefmt='psql'))
    else:
        print("\n No patients found with the given ID.")
    
    
    
    
def delete_patients(cursor,db):
    patient_id=int(input('Enter the Patient ID = '))
    cursor.execute('delete from patients where pid =%s',(patient_id,))
    commit_message(cursor,db,'One record deleted .')
    view_patients(cursor,db)


def view_patients(cursor,db):
    cursor.execute('select * from patients')
    result=cursor.fetchall()
    
    columns=["Patients_ID","Name","Age","Gender","Contact"]
    print(tabulate(result,headers=columns,tablefmt='psql'))
    
    
def patients_menu(cursor,db):
    while True:
        print('\n **Patient Menu** ')
        print('\n 1. Add Patient')
        print(' 2. Update Patient')
        print(' 3. Delete Patient')
        print(' 4. View Patient')
        print(' 5. Exit to Main Menu')
        
        choice=input('\nEnter Your Choice = ')
        
        if choice == '1':
            add_patients(cursor,db)
        elif choice == '2':
            update_patients(cursor,db)
        elif choice == '3':
            delete_patients(cursor,db)
        elif choice == '4':
            view_patients(cursor,db)
        elif choice == '5':
            break
        else:
            print('Invalid Choice....')
            

#________________________________________________Doctor Management__________________________________________________

def add_doctor(cursor,db):
    while True:
        name=input('Enter the Doctor Name = ').title().strip()
        Specialization=input('Enter the specialization = ').title().strip()
        
        cursor.execute('insert into doctors (name,specialization)values(%s,%s)',(name,Specialization))
        commit_message(cursor,db,'Data inserted successfully')
        view_doctor(cursor,db)
        
        result=input('Are you sure you want to add Doctor? (yes/no): ').title().lower()
        
        if result == 'no':
            break
    
def update_doctor(cursor,db):
    doctor_id=int(input('Enter the Doctor Id = '))
    
    name=input('Enter the Doctor Name = ').title().strip()
    Specialization=input('Enter the specialization = ').title().strip()
    
    cursor.execute('update doctors set name=%s,specialization=%s where d_id=%s',(name,Specialization,doctor_id))
    commit_message(cursor,db,'One record updated.')
    
    cursor.execute('select * from doctors where d_id=%s',(doctor_id))
    result=cursor.fetchone()
    
    if result:
        columns=["Doctor_ID","Name","Specialization"]
        print(tabulate([result],headers=columns,tablefmt='psql'))
    else:
        print("\n No Doctor found with the given ID.")
        
    
    
    
def delete_doctor(cursor,db):
    doctor_id=int(input('Enter the Doctor Id = '))
    
    cursor.execute('delete from doctors where d_id=%s',(doctor_id,))
    commit_message(cursor,db,'One record deleted.')
    view_doctor(cursor,db)
    

def view_doctor(cursor,db):
    cursor.execute('select * from doctors')
    result=cursor.fetchall()
    
    columns=["Doctor_ID","Name","Specialization"]
    print(tabulate(result,headers=columns,tablefmt='psql'))
    
def doctor_menu(cursor,db):
    
    while True:
        print('\n **Doctor Management**')
        print('\n 1. Add Doctor')
        print(' 2. Update Doctor')
        print(' 3. Delete Doctor')
        print(' 4. View Doctor')
        print(' 5. Exit To Main Menu')
        
        choice=input('\nEnter Your Choice = ')
        
        if choice == '1':
            add_doctor(cursor,db)
        elif choice == '2':
            update_doctor(cursor,db)
        elif choice == '3':
            delete_doctor(cursor,db)
        elif choice == '4':
            view_doctor(cursor,db)
        elif choice == '5':
            break
        else:
            print('Invalid Choice....')

#________________________________________________ Appointment Management ________________________________

def book_appointment(cursor,db):
    
    while True:
    
        patient_id=int(input('Enter the patient ID : '))
        doctor_id=int(input('Enter the Doctor ID : '))
        
        cursor.execute('insert into patient_doctor(patient_id,doctor_id) values(%s,%s)',(patient_id,doctor_id))
        commit_message(cursor,db,'Appointment Booked successfully')
        view_appointment(cursor,db)
        
        result=input('Do you want to Book another Appointment? (yes/no) = ').strip().lower()
        
        if result == 'no':
            break
        
    
    
    
def update_appointment(cursor,db):
    appointment_id=int(input('Enter the Appointment ID : '))
    
    patient_id=int(input('Enter the New Patient ID : '))
    doctor_id=int(input('Enter the New Doctor ID : '))
    
    cursor.execute('update patient_doctor set patient_id=%s,doctor_id=%s where pd_id=%s',(patient_id,doctor_id,appointment_id))
    
    commit_message(cursor,db,'One record updated.')
    
    cursor.execute('select * from patient_doctor where pd_id=%s',(appointment_id,))
    result=cursor.fetchone()
    
    if result:
        columns=['Appointment_Id','Patient Name' ,'Doctor Name' ]
        print(tabulate([result],headers=columns,tablefmt='psql'))

def cancel_appointment(cursor,db):
    
    appointment_id=int(input('Enter the Appointment ID : '))
    
    cursor.execute('delete from patient_doctor where pd_id=%s',(appointment_id))
    commit_message(cursor,db,'Appointment Cancelled successfully')
    view_appointment(cursor,db)
    
def view_appointment(cursor,db):
    
    cursor.execute('select a.pd_id, p.name as patients ,d.name as doctors from patient_doctor a join patients p on a.patient_id=p.pid join doctors d on a.doctor_id=d.d_id')
    
    result=cursor.fetchall()
    columns=['Appointment_Id','Patient Name' ,'Doctor Name' ]
    print(tabulate(result,headers=columns,tablefmt='psql'))
    
    
def appointment_menu(cursor,db):
    while True:
        print('\n **Appointment Management**')
        print(' \n1.Book Appointment')
        print(' 2.Update Appointment ')
        print(' 3.Delete Appointment ')
        print(' 4.View Appointment ')
        print(' 5. Exit To Main Menu')
        
        choice=input('\nEnter Your Choice = ')
        
        if choice == '1':
            book_appointment(cursor,db)
        elif choice == '2':
            update_appointment(cursor,db)
        elif choice == '3':
            cancel_appointment(cursor,db)
        elif choice == '4':
            view_appointment(cursor,db)
        elif choice == '5':
            break
        else:
            print('Invalid Choice....')
        

#__________________________________________________________________________________________________________________

def main_menu():
    db=connect_db()
    cursor=db.cursor()
    
    if not login(cursor):
        return
    
    while True:
        print('\n**Hospital Patient Management System **')
        print('\n 1.Patient Management')
        print(' 2.Doctor Management')
        print(' 3.Appointment Management')
        print(' 4.Exit ')
        
        choice=input('\nEnter Your Choice = ')
        
        if choice == '1':
            patients_menu(cursor,db)
        elif choice == '2':
            doctor_menu(cursor,db)
        elif choice == '3':
            appointment_menu(cursor,db)
        elif choice == '4':
            print('Exiting Program ......')
           
            break
        else:
            print('Enter proper choice')
            
if __name__ == '__main__':
    main_menu()


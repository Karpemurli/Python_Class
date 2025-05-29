import pymysql as ss
from dotenv import load_dotenv
from tabulate import tabulate
import os
import pyautogui
from datetime import datetime


load_dotenv()
my_password =os.getenv("db_pass")

# print(my_password)


def connect_db():
    return ss.connect(host='localhost',user='root',passwd=my_password,database='hospital_db')


def commit_message(cursor,db,message):
    db.commit()
    print(message)
    
#____________________________ Login _______________________________________


def login(cursor):
    while True:
        uname=input('Enter the username = ').strip()
        upass=pyautogui.password(text="Enter the user password : ",title= "Enter Password  ",default= '',mask='*')
        cursor.execute("select * from users where uname=%s and password=%s",(uname,upass))
        
        user=cursor.fetchone()
        
        if user:
            print("Login success welcome" + uname)
            return True
        else:
            print("Invalid username and password please check again....")
        
#__________________________ Patients Management _________________________________



def add_patients(cursor,db):
    while True:
        name=input('\nEnter the patient name = ').title().strip()
        age=int(input('Enter the patient age = '))
        gender=input('Enter the patient gender (Male/Female/Other) = ').title().strip()
        contact=input('Enter the Contact = ')
        address=input('Enter the address= ').title().strip()
        disease=input('Enter the Disease = ').title().strip()
        date_time=datetime.now()
        
        cursor.execute("insert into patients(name,age,gender,contact,address,disease,admitted_date) values(%s,%s,%s,%s,%s,%s,%s)",(name,age,gender,contact,address,disease,date_time))
        
        commit_message(cursor,db,'\nData Inserted Successfully')
        view_patients(cursor,db)
        result=input('Do you want to add another patient? (yes/no) = ').strip().lower()
        
        if result == 'no':
            break
        
        

    
        
def update_patients(cursor,db):
    
    patient_id=int(input('\nEnter the Patient Id = '))
    
    name=input('\nEnter the New patient name = ').title().strip()
    age=int(input('Enter the New patient age = '))
    gender=input('Enter the New patient gender (Male/Female/Other) = ').capitalize().strip()
    contact=input('Enter the New Contact = ').strip()
    address=input('Enter the New address= ').title().strip()
    disease=input('Enter the New Disease = ').title().strip()
    date_time=datetime.now()
    new_date_time=date_time.strftime("%Y-%m-%d-%H:%M:%S")
    
    
    cursor.execute('update patients set name=%s, age=%s, gender=%s,contact=%s,address=%s,disease=%s,updated_datetime=%s where p_id=%s',(name,age,gender,contact,address,disease,new_date_time,patient_id))
    commit_message(cursor,db,'One record Updated')
    
    
    
    cursor.execute('select * from patients where p_id =%s',(patient_id,))
    result=cursor.fetchone()
    if result:
        columns=['Patient_ID',"Name","Age","Gender","Contact","Address","Disease","admitted_date","Updated_Date"]
        print(tabulate([result],headers=columns,tablefmt='psql'))
    else:
        print("\n No patients found with the given ID.")
    
    
    
    
    

    
def delete_patients(cursor,db):
     patient_id=int(input('Enter the Patient Id = '))
     
     cursor.execute('delete from patients where p_id=%s',(patient_id))
     commit_message(cursor,db,'One record deleted.')
     view_patients(cursor,db)
     

def view_patients(cursor,db):
    cursor.execute('select * from patients ')
    result=cursor.fetchall()
    columns=['Patient_ID',"Name","Age","Gender","Contact","Address","Disease","Admitted_Date","updated_datetime"]
    print(tabulate(result,headers=columns,tablefmt="psql"))
     
     
def patients_menu(cursor,db):
    while True:
        print("\n ** Patients Menu ** ")
        print('\n 1.Add Patient ')
        print(' 2.Update Patient')
        print(' 3.Delete Patient')
        print(' 4.Display Patient')
        print(' 5.Exit To Main Menu')
        
        choice=input("\n Enter Your Choice = ")
        
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
            
#___________________________________________  Doctor Management _____________________________


def add_doctor(cursor,db):
    while True:
        name = input('\nEnter the  Doctor Name :').title().strip()
        specialization=input('Enter the specialization :').upper().strip()
        contact=input('Enter the Contact = ')
        
        cursor.execute('insert into doctors(name,specialization,contact) values(%s,%s,%s)',(name,specialization,contact))
        commit_message(cursor,db,'\nData Inserted Successfully')
        view_doctors(cursor,db)
        result=input('Do you want to add another Doctor? (yes/no) = ').strip().lower()
        
        if result == 'no':
            break
        
def update_doctors(cursor,db):
    doctors_id=int(input('\nEnter the doctors Id = '))
    
    
    name = input('\nEnter the new  Doctor Name :').title().strip()
    specialization=input('Enter the new specialization :').upper().strip()
    contact=input('Enter the new Contact = ')
    
    
    cursor.execute('update doctors set name=%s,specialization=%s,contact=%s where d_id=%s',(name,specialization,contact,doctors_id))
    
    commit_message(cursor,db,'One record updated')
    
    
    #display update record....
    
    cursor.execute('select * from doctors where d_id=%s',(doctors_id,))
    result=cursor.fetchone()
    
    if result:
        columns=['D_ID','Doctors', 'Specialization', 'Contact']
        print(tabulate([result],headers=columns,tablefmt='psql'))
    else:
        print("\n No Doctors found with the given ID.")
    
        

    
def delete_doctors(cursor,db):
    doctors_id=int(input('Enter the doctors Id = '))
    
    cursor.execute('delete from doctors where d_id =%s ',(doctors_id))
    commit_message(cursor,db,'One record deleted.')
    view_doctors(cursor,db)
    
    
def view_doctors(cursor,db):
    
    cursor.execute('select * from Doctors')
    result=cursor.fetchall()
    column=['Doctor_Id','Name','Specialization','Contact']
    print(tabulate(result,headers=column,tablefmt='psql'))
    
    
def doctors(cursor,db):
    while True:
        print("\n ** Doctors Menu **")
        print('\n 1.Add Doctor ')
        print(' 2.Update Doctor')
        print(' 3.Delete Doctor')
        print(' 4.Display Doctor')
        print(' 5.Exit To Main Menu')
        
        choice=input("\nEnter Your Choice = ")
        
        if choice == '1':
            add_doctor(cursor,db)
        elif choice == '2':
            update_doctors(cursor,db)
        elif choice == '3':
            delete_doctors(cursor,db)
        elif choice == '4':
            view_doctors(cursor,db)
        elif choice == '5':
            break
        else:
            print('Invalid Choice....')
        
        
    
    
    



#___________________________________________ Appointment  Management ________________________



def book_appointment(cursor,db):
    while True:
        patent_id=int(input('Enter Patient ID :'))
        doctor_id=int(input('Enter Doctor ID : '))
        appoinment_date=datetime.now()
        status=input('Enter Status (scheduled,completed,cancelled) :').capitalize().strip()
        
        
        cursor.execute('insert into appointments(patient_id,doctor_id,appointment_date,status) values(%s,%s,%s,%s)',(patent_id,doctor_id,appoinment_date,status))
        commit_message(cursor,db,'Appointment Booked Successfully')
        
        
        view_appointments(cursor,db)
        
        result=input('Do you want to Book another Appointment? (yes/no) = ').strip().lower()
        
        if result == 'no':
            break


def update_appoinments(cursor,db):
    appointment_id=int(input("Enter the Appointment_ID = "))
    
    patent_id=int(input('Enter New Patient ID :'))
    doctor_id=int(input('Enter New Doctor ID : '))
    appoinment_date=datetime.now()
    new_appoinment_date=appoinment_date.strftime("%Y-%m-%d-%H:%M:%S")
    status=input('Enter Status (scheduled,completed,cancelled) :').capitalize().strip()
    
    
    cursor.execute('update appointments set patient_id=%s,doctor_id=%s,appointment_date=%s,status=%s where a_id=%s ',(patent_id,doctor_id,new_appoinment_date,status,appointment_id))
    commit_message(cursor,db,'One record updated')
    
    
    cursor.execute('select * from appointments where a_id=%s',(appointment_id,))
    
    result=cursor.fetchone()
    
    if result:
        columns=['Ap_ID','Patient ID','Doctor ID','Date','Status']
        print(tabulate([result],headers=columns,tablefmt='psql'))
    else:
        print("\n No Appointments found with the given ID.")
    
    
    
    
    
    
def cancel_appointment(cursor,db):
    
    appointment_id=int(input('Enter the Appointment_Id ='))
    
    cursor.execute('update appointments set status=%s where a_id=%s',('cancelled',appointment_id))
    commit_message(cursor,db,'Appointment Cancelled Successfully')
    
        
        
        
        
def view_appointments(cursor,db):
    cursor.execute('select a.a_id, p.name as patients, d.name as doctors ,a.appointment_date,a.status from appointments a join patients p on a.patient_id=p.p_id join doctors d on a.doctor_id=d.d_id ')
    
    
    result=cursor.fetchall()
    column=['Appointment ID','patient Name','Doctor Name','Date','Status']
    print(tabulate(result,headers=column,tablefmt='psql'))  
    
    
    
def appointments(cursor,db):
    while True:
        print("\n ** Appointment Menu **")
        print('\n 1.Book Appointment ')
        print(' 2.Update Appointments')
        print(' 3.Cancel Appointments')
        print(' 4.View Appointments')
        print(' 5.Exit To Main Menu')
        
        choice=input("\nEnter Your Choice = ")
        
        if choice == '1':
            book_appointment(cursor,db)
        elif choice == '2':
            update_appoinments(cursor,db)
        elif choice == '3':
            cancel_appointment(cursor,db)
        elif choice == '4':
            view_appointments(cursor,db)
        elif choice == '5':
            break
        else:
            print('Invalid Choice....')
    
    
    

#________________________________________ __ Billing Management _______________________________


def generate_bill(cursor,db):
    
    patients_id=int(input('Enter Patient ID: '))
    total_amount=float(input('Enter Total Amount: '))
    date=datetime.now()
    
    cursor.execute('Insert into bills (patient_id,total_amount,billing_date)values(%s,%s,%s)',(patients_id,total_amount,date))
    commit_message(cursor,db,'Bill Generated Successfully')
    
    cursor.execute('select b.b_id, p.name as patients, b.total_amount, b.billing_date from bills b join patients p on b.patient_id=p.p_id where b.patient_id=%s',(patients_id,))
    
    result=cursor.fetchone()
    
    if result:
        columns=['Bill ID','Patient Name','Total Amount','Billing Date']
        print(tabulate([result],headers=columns,tablefmt='psql'))
    else:
        print("\n No Bills found for the given Patient ID.")
        
    
    
    
    
def update_bills(cursor,db):
    
    bill_id=int(input('Enter Bill Id to update ='))
    
    new_amount=float(input('Enter Amount to update = '))
    new_status=input('Enter Patient Status to update =')
    bill_date=datetime.now()
    new_bill_date=bill_date.strftime("%Y-%m-%d-%H:%M:%S")
    
    cursor.execute('update bills set total_amount=%s,status=%s,billing_date=%s where b_id=%s',(new_amount,new_status,new_bill_date,bill_id))
    commit_message(cursor,db,'Bill Updated Successfully')
    
    cursor.execute('select * from bills where b_id=%s',(bill_id))
    
    result=cursor.fetchone()
    
    if result:
        columns=['Bill ID','Patient Name','Total Amount','Status','Billing Date']
        print(tabulate([result],headers=columns,tablefmt='psql'))
    else:
        print("\n No bill found with the given ID.")
            
    
    
    
    
    
    
def pay_bill(cursor,db):
    bill_id=int(input('Enter Bill ID to mark as Paid = '))
    cursor.execute('update bills set status=%s where b_id =%s',('paid',bill_id))
    commit_message(cursor,db,'Bill Status updated to Paid')
    
    
def view_bills(cursor,db):
    
    cursor.execute('select b.b_id, p.name,b.total_amount,b.status,b.billing_date from bills b join patients p on b.patient_id=p.p_id')
    
    result=cursor.fetchall()
    columns=['Bill ID','Patient Name','Total Amount','Status','Billing Date']
    print(tabulate(result,headers=columns,tablefmt='psql'))

            
            
def Billingmng(cursor,db):
    while True:
        print("\n ** Billing Management **")
        print('\n 1.Generate Bill ')
        print(' 2.Update Bills')
        print(' 3.Pay Bill')
        print(' 4.View Bill')
        print(' 5.Exit To Main Menu')
        
        choice=input("\nEnter Your Choice = ")
        
        if choice == '1':
            generate_bill(cursor,db)
        elif choice == '2':
            update_bills(cursor,db)
        elif choice == '3':
            pay_bill(cursor,db)
        elif choice == '4':
            view_bills(cursor,db)
        elif choice == '5':
            break
        else:
            print('Invalid Choice....')
    
    
            
#_______________________________Main menu ____________________________________________


def main_menu():
    db=connect_db()
    cursor=db.cursor()
    
    if not login(cursor):
        return
    while True:
        print("\n ** Main Menu ** ")
        print('\n 1.Patient Management')
        print(' 2.Doctor Management')
        print(' 3.Appointment Management')
        print(' 4.Billing Management')
        print(' 5.Exit To Main Menu')
        
        choice=input("\nEnter Your Choice = ")
        
        if choice == '1':
            patients_menu(cursor,db)
            
        elif choice == '2':
            doctors(cursor,db)
        elif choice == '3':
            appointments(cursor,db)
        elif choice == '4':
            Billingmng(cursor,db)
        elif choice == '5':
            print('Exiting Program ......')
            break
        else:
            print('Enter Proper Choice ')
            
            
if __name__ == '__main__':
    main_menu()
            
     
    
    
    
    
    
                                     
    
    
    
    
        
        

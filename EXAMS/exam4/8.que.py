# 8)	Write a program to enter names of employees and their salaries as input and store them in a dictionary.


emp_data={}

num_employees=int(input("Enter the number of employe:"))

for i in range(num_employees):
    name=input("Enter emp name:")
    salary=float(input("Enter salary: "))
    emp_data[name]=salary


print("\nEmployee Data:")
for name,salary in emp_data.items():
    print(f"Name:{name},salary:{salary}")
# question=5

symptoms={
    
    "Fever":"You may need to take rest and hydrate and take tablets prescribed by doctor as per instructions",
    "cough":"Drink warm fluids ,Don't eat oily ,spicy food and take cough syrup and tables prescribed by doctor as per instructions",
    "Headache":"Try resting in a dark room and take cough syrup and tablets prescribed by doctor as per instructions"
        
}
Name=input('Enter the name=')
symptoms=input('Enter Symptoms(Fever,Cough,Headache)=')

age =int(input('Enter the age='))




if age < 5:
    fees='No fees'
elif age < 10:
    fees='RS.  50'
elif age < 18:
    fees='RS.  100'
elif age < 40:
    fees='RS.200'
elif age < 60:
    fees='RS. 150'
else:
    fees='No fees'
    


print('Name:',Name)
print('Symptoms:',symptoms)
print('Age:',age)

print('Consultative Fees:',fees)
print('Instructions:',symptoms)


    

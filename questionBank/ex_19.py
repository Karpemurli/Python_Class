# 19. A company decided to give bonus to employee according to following criteria:
#     Time period of Service                           Bonus
#     More than 10 years                                   10%
#     >=6 and <=10                                             8%
#     Less than 6 years                                      5%

salary=float(input('Enter the employee salary:'))
Sevices_year =int(input('Enter Your Servics Period(Years):'))


if Sevices_year > 10:
    bonus_percentage=10
elif 6 <= Sevices_year <= 10:
    bonus_percentage=8
else:
    bonus_percentage=5 #service_year <6


Bonus=(bonus_percentage/100)*salary

print(f"The employee gets a bonus of {bonus_percentage}%.")

print(f"The Bonus amount is:${Bonus:.2f}")

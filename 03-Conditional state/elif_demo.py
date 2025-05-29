
# elif statement

python=int(input("Enter the mark of  Python out of 100:"))
Java=int(input("Enter the mark of Java out of 100:"))
Mern=int (input("Enter the mark of Mern out of 100:"))

Total=python+Java+Mern
print("Total Mark:",Total)

avg=Total/3
print("Percentage:",avg)


    

if 90 <= avg <= 100:
    print("Grade: A")
elif 60 <= avg < 90:
    print("Grade: B")
elif 35 <= avg < 60:
    print("Grade: C")
else:
    print("Grade: Fail")


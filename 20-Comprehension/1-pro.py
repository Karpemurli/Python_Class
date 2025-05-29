
'''

List Comprehension
_________________________________

lst name=[expression for item in iterable if condition]

'''

lst = [1,2,3,4]

# Square each number in the list
new_list= [x ** 2 for x in lst]
print(" Square root =" ,new_list)

newlst=[ x for x in lst if x%2==0  ]; print("Even :" ,newlst)

#_______________________________________________________________________

text= " Hello World"
newlist= [char for char in text if char.lower() in "aeiou"]
print(newlist)

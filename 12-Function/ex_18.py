# Write a program to read 6 numbers 
# and create a dictionary having keys EVEN and ODD. 
# Dictionary's value should be stored in list. 
# Your dictionary should be like:
# {'EVEN':[8,10,64], 'ODD':[1,5,9]}


def main(num):
    
    Dic={"EVEN":[],"ODD":[]}
    
    for i in num:
        if i % 2 == 0:
            Dic['EVEN'].append(i)
        else:
            Dic['ODD'].append(i)
    return Dic


# num=[8,10,64,1,5,9]
num=[int(input(f"Enter the number{i+1}:"))for i in range(6)]

ans=main(num)
print(ans)            

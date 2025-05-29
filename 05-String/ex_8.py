# Write a Python program to remove repeated consecutive characters and replace them with single letters and print a updated string.
# Sample Data:
# ("Red Green White") -> "Red Gren White"
# ("aabbbcdeffff") -> "abcdef"
# ("Yellowwooddoor") -> "Yelowodor"



    
data = ["Red Gren White", "aabbbcdeffff","Yellowwooddoor"]
for i in data:
    final_str = ""
    for s in range(len(i)):
        if s==0 or i[s]!=i[s-1]:
            final_str = final_str + i[s]
    print(f'Original String:{i} ----> Updated String :{final_str}')



# str1 = "23333"
# result=str1[0]

# for i in range(1,len(str1)):
#     if str1[i] != str1[i-1]:
#         result += str1[i]
        
# print(result)

# str2="aabbbcdeffff"
# result2=str2[0]

# for i in range(1,len(str2)):
#     if str2[i] != str2[i-1]:
#         result2 += str2[i]
# print(result2)

# str3="Yellowwooddoor"
# result3=str3[0]

# for i in range(1,len(str3)):
#     if str3[i] != str3[i-1]:
#         result3 += str3[i]
# print(result3)
    
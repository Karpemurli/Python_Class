# 2.	How can you find the maximum and minimum values in a list without using max() and min() functions?


def find_num(list_nm):
    min_num = list_nm[0]
    max_num = list_nm[0]
    
    for i in list_nm:
        if i > max_num:
            max_num = i
        if i < min_num:
            min_num = i
    return max_num, min_num

list_nm = [101,205,40,58,77,99,102]


min_num,max_num = find_num(list_nm)

print("Minimum number is:", min_num)

print("Maximum number is:", max_num)
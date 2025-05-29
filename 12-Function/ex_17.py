# 2. Write a program to print all elements in a list those have only single occurrence.
# Example: if contents of list is [7, 5, 5, 1, 6, 7, 8, 7, 6].
# Your output should be:
# 1 8


def main():
    list_nums = [7, 5, 5, 1, 6, 7, 8, 7, 6]
    print(f'Original list=',list_nums)
    single_value =[]
    
    for i in list_nums:
        if list_nums.count(i) == 1:
            single_value.append(i)
    return single_value

Ans=main()

print(f"Output:",Ans)


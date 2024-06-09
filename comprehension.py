# List_of_Number= [1,2,3,4]
# List_of_Square_of_num = [ ]

# for i in List_of_Number:
#     s=i**2
#     List_of_Square_of_num.append(s)

# print(List_of_Square_of_num)

# Calculate square of numbers using list comprehension 
# List_of_Number= [1,2,3,4,5,6]

# # list_of_square_of_num=[ expression for item in sequence if condition ] -------> Basic syntax 

# list_of_square_of_num=[num**2 for num in List_of_Number]
# print(f"The list of square number is: {list_of_square_of_num}")

# list_of_square_of_even_num =[num**2 for num in List_of_Number if num %2==0]
# print(f"The list of square is even number is: {list_of_square_of_even_num}")


# without Set Comprehension 

# Set_of_num = {1,2,3,4}
# # print(type(Set_of_num))
# set_of_square_of_num = set()

# for num in Set_of_num:
#     num=num**2
#     set_of_square_of_num.add(num)

# print(set_of_square_of_num)

# With set comprehension 
# Set_of_num = {1,2,3,4}
# set_of_square_of_num = {num**2 for num in Set_of_num}
# print(Set_of_num)

# set_of_square_of_even_num = {n**2 for n in Set_of_num if n%2==0}
# print(set_of_square_of_even_num)


# # Without Dictionary Comprehension 
# ori_dict= {"a":1 , "b":2, "c":3}

# # Creating a new dictionary in which key-value pairs are swapped version of ori_dict

# new_dict={}

# for key,value in ori_dict.items():
#     new_dict[value]=key

# print(new_dict)

# Using dictionary Comprehension:
# Syntax for comprehension of dictionary=== new_dict={key: expression for item in sequence if condition}

# ori_dict= {"a":1 , "b":2, "c":3}
# new_dict={value:key for key,value in ori_dict.items() }
# print(new_dict)

# Create a new dictionary in which only even values from ori dict are stored after squaring 

ori_dict= {"a":1 , "b":2, "c":3 ,"d":4}
new_dict={key:value**2 for key,value in ori_dict.items() if value%2==0}
print(new_dict)

















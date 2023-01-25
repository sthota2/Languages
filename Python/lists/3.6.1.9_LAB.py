my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
unique_list = []
for i in range(len(my_list)):
    if (my_list[i]) not in unique_list:
        unique_list.append(my_list[i])
    elif (my_list[i]) in my_list:
        pass
#
print("The list with unique elements only:",unique_list)
print(my_list)

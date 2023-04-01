#declare list 
my_list = [1, 2, 3, "four", "five"]


# accessing list items
my_list[0]
my_list[-1]

#list slicing
my_list[2:4]

my_list[1] = 10  # Modifies the second element in the list
my_list.append(6)  # Adds the value 6 to the end of the list
my_list.insert(2, "three")  # Inserts the value "three" at index 2
my_list.remove("four")  # Removes the first occurrence of the value "four" from the list


for element in my_list:
    print(element)

#to check the size of list we use "len" function
print(len(my_list))
my_list = [1, 2, 3]

my_mixed_list = ["STRING", 100, 22.22]

print(len(my_list))

#indexing and slicing works just as in strings
print(my_mixed_list[0])

print(my_list[1:])

print(my_list[::-1])

#Concatenation
print(my_list+my_mixed_list)
print(my_list)
print(my_mixed_list)

#Lists are mutable as opposed to Strings
my_list[0] = "CHANGED ELEMENT"
print(my_list)

#in place modification of list
my_list.append(4)
my_list.append(5)

print(my_list)

#remove elements from end
popped_item = my_list.pop()
print(popped_item)
print(my_list)


print(f'{my_list.pop(2)} {my_list}')

#sort method doesn't return anything
my_int_list = [34,22,11,34,56,67]
my_int_list.sort()
print(my_int_list)
my_int_list.reverse()
print(my_int_list)

my_new_list = [1]*5
print(my_new_list)
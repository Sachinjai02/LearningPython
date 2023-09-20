#Tuples are similar to lists but they are immutable
my_tup = (1,"2",3.0)
my_list = [1,2,3]

print(type(my_tup))
print(type(my_list))

#supports slicing and indexing
print(my_tup[0])
print(my_tup[::-1])

#has couple of functions - count and index
print(my_tup.count("2")) # returns count of occurrence of "2" in the tuple
print(my_tup.index(1)) #returns first index of this element

#immutability
#my_tup[0] = 11 -- tuple does not support item assignment
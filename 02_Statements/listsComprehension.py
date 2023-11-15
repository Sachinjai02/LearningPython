mystring = 'hello'
mylist = []
for _ in mystring:
    mylist.append(_)

print(mylist)

# using list comprehension to achieve above
mylist = [letter for letter in mystring]  # flattened out for loop
print(mylist)

mylist = [letter for letter in 'HelloWorld']
print(mylist)

mylist = [num ** 2 for num in range(1, 11)]
print(mylist)

# list comprehension with filter
mylist = [num for num in range(1, 11) if num % 2 == 0]
print(mylist)

# list comprehension with if else
mylist = [x if x % 2 == 0 else x + 1 for x in range(0, 11)]
print(mylist)

#list comprehension with nested for loops
mylist = [x*y for x in [1, 2, 3] for y in [1, 10, 1000]]
print(mylist)

mylist.insert(1,12)

print(mylist)

help(mylist.insert)
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


print([l for l in "Sachin"])
print([x for x in range(1,11, 2)])
print([x*2 for x in range(1,11) if x % 2 == 0])
print([m for m in zip(range(1,10), range(0,9))])

st = "Print only the words that start with s in this sentence"
words = st.split(" ")
for word in words:
    if len(word)%2 == 0:
        print(word)


print([s[0] for s in words])
print([l for l in range(1, 51) if l % 3 == 0])
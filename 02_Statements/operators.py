from random import shuffle, randint

# range operator
# start from 0 to 10(but don't include 10)
for num in range(10):
    print(num)
# start from 4 to 10 (don't include 10)
for num in range(4, 10):
    print(num)

# range operator with step size; its a generator
for num in range(2, 11, 2):
    print(num)

# this just returns the range operator
print(range(2, 11, 2))

# to  get a list from range we will need to cast it to list explicitly
my_list = list(range(0,11,2))
print(my_list)

# Enumerate fn

# Use case
index = 0
word = 'Sachin'
for charac in word:
    print(f'index of letter {charac} is {index}')
    index += 1

# Better implementation using enumerate
for enumTuple in enumerate(word):
    print(enumTuple)

#tuple unpacking
for indx, letter in enumerate(word):
    print(f'index of letter {word[indx]}/{letter} is {indx}')

## opposite of enumerate -> zip
mylist1 = [1, 2, 3, 4, 5, 6]
mylist2 = ['a', 'b', 'c']
mylist3 = [1111, 2222, 3333]

#zip goes as far as the shortest list
for item in zip(mylist1, mylist2,  mylist3):
    print(item)

print(list(zip(mylist1, mylist2)))

# in operator to check if an element is present in an iterable object
print('x' in ['x', 'y', 'z'])
print( (1, 2) in [(1, 2), (3, 4), (2, 1)])
print ('a' in 'Sachin')

print( 'k1' in {'k1':'true'})
print( 'k1' in {'k1':'true'}.keys())
print (345 in {'h1':345}.values())

print(f' check if 1== "1" {1=="1"}')
print(f' check if 1== 1.0 {1==1.0}')

# min, max function in list
print(min(['x','y','z']))
print(max(['sachin','troshi','xylo']))
print(min('sachin'))
print(max([12,12,34,35,55,2]))

mylist = [1,2,3,4,5,6,7,8,9,10]
#in place function to shuffle the list; doesn't return anything
shuffle(mylist)
print(mylist)
shuffle(mylist)
print(mylist)

#get a random number
print(randint(0,100))

#ask for user input; it always return result in a string
inputnum = input('Enter a number here: ')
inputname = input('What is your name: ')

print(type(inputnum))
print(inputnum)
print(int(inputnum))
print(inputname)
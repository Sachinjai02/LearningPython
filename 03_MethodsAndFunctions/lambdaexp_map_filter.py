#use of map
def square(num):
    return num**2

my_nums = [1, 2, 3, 4, 5]

my_nums_sq = list(map(square, my_nums))
for item in map(square, my_nums):
    print(item)


def splicer(mystring):
    if len(mystring) %2 == 0:
        return 'Even'
    else:
        return mystring[0]

names = ['Sachin', 'Andy', 'Eve', 'Sally']

print(list(map(splicer, names)))

#use of filter
def check_even(n):
    return n%2 == 0

list_nums = [1, 2, 3, 4, 5, 6, 7]
print(list(filter(check_even, list_nums)))


# Lambda expressions
def cube(n):
    return n**3

#turn above fn to lambda exp
#lambda exp is also known as an annonymous fn
cube = lambda num: num ** 3
cube(5)

print(list(map(lambda n, n2=89: n*n2, list_nums)))
print(list(filter(lambda n: n%2 == 0, list_nums)))


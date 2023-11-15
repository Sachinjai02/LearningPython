def say_hello(name):
    """
    This is my first function
    :return: doesn't return anything
    """
    print(f"Hello {name}")
    print("Hello again {n}".format(n=name))


def add(n1, n2=100):
    """
    Returns sum of two numbers
    :param n1:
    :param n2:
    :return:
    """
    return n1 + n2


def isEven(num):
    if num % 2 == 0:
        return True
    return False

def check_even_list(list):
    for num in list:
        if num % 2 == 0:
            return True

def filter_evens(list):
    return [x for x in list if x % 2 == 0]

say_hello("Sachin")
sum = add(10, 20)
print(sum)
print(add(500))

for num in range(23, 99):
    print(f'is {num} Even? : {isEven(num)}')

print(check_even_list([1, 3, 5])) ##None

print (filter_evens([2,3,4,5,6,7]))
print (filter_evens([1,3,5]))
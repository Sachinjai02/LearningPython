import re
import json

input_string = "I am special \<string\>"
print(len(input_string))
json_data = {"hello": input_string}
for (indx, char) in enumerate(input_string):
    print(f'char at index {indx} is {char}')


# Use snake lower casing for naming functions
def say_hello(name='Def:Sachin'):
    """
    This is my first function
    :return: doesn't return anything
    """
    print(f"Hello {name}")
    print("Hello again {n}".format(n=name))


def unescape_special_characters(escaped_string):
    unescaped_string = re.sub(r'\\([{}<>])', r'\1', escaped_string)
    return unescaped_string


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
say_hello()
sum = add(10, 20)
print(sum)
print(add(500))

for num in range(23, 99):
    print(f'is {num} Even? : {isEven(num)}')

print(check_even_list([1, 3, 5]))  ##None

print(filter_evens([2, 3, 4, 5, 6, 7]))
print(filter_evens([1, 3, 5]))

# Example usage:
escaped_string = "This \\{ is a \\} sample \\<string\\> with special characters and tokens <TOKEN1> and {TOKEN2}."
unescaped_result = unescape_special_characters(escaped_string)

print("Escaped string:", escaped_string)
print("Unescaped string:", unescaped_result)

mystr = input("Enter a string")
print({'k':mystr})
print(unescape_special_characters(mystr))

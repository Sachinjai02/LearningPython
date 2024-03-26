def func():
    return 1


def hello(name='Sachin'):
    print("The hello() function has been executed")

    def greet():
        return "\t This is the greet() function inside hello!"

    def welcome():
        return '\t This is welcome() inside hello!'

    print("This returns a function!")
    if name == 'Sachin':
        return greet
    else:
        return welcome

def other_func(some_def_func):
    print("Other code runs here!")
    print(some_def_func())

var = func
val_val = var()
print(val_val)
var = hello()
print(var())

other_func(hello)
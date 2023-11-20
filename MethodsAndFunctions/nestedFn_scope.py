#LEGB RULES
#L: Local to fn or lambda
#E: Enclosing fn
#G: Global
#B: Built-in keywords

#GLOBAL
x = 1000
y = 1234

def my_func():

    #This is an enclosing variable
    x = 100
    y = 'changed' # This is still a local var to my_func()
    def my_inner_fun():
        global y # This is global variable y
        # and any changes to this val in this function would reflect to original y's scope

        # This is a local variable
        x = 10
        y = 'changed further'
        print(f'I am printing local variable x: {x}')
        return x
    print(f'I am printing enclosing var x: {x}')
    my_inner_fun()
    print(f'This shouuld be local variable y: {y}')
    return x

print(f'original value for y:  {y}')
print(f'I am printing global variable x: {x}')
my_func()
print(f'updated value for y after fn call :  {y}')

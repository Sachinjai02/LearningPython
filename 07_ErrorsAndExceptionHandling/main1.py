def add (n1, n2):
    return n1 + n2

num1 = 10
#num2 = input("Please enter a number: ")
num2 = 20
try:
    result = add(num2, num1)
except:
    print('An error occurred in addition')
else:
    print("Add went well! Result is {}".format(result))
finally:
    print("This should be executed always!")
class MyFirstClass():
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

    def my_method(self):
        print(f'object variables for this instance is {self.param1} and {self.param2}')


my_sample = MyFirstClass(10,20)

print(type(my_sample))
print(my_sample)
my_sample.my_method()
from base import Animal


class Dog(Animal):

    def __init__(self):
        # super().__init__()
        Animal.__init__(self)
        print("Dog created")

    def who_am_i(self):
        print("I am a dog")

    def bark(self):
        print("WOOF!")

    def eat(self):
        print("Dog is eating")


my_dog = Dog()
my_dog.who_am_i()
my_dog.eat()
my_dog.bark()

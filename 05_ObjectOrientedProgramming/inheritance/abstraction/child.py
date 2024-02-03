from base import Animal


class Dog(Animal):

    def __init__(self, name):
        Animal.__init__(self, name)

    def speak(self):
        return self.name + " says woof!! "

my_dog = Dog("Frankie")
print(my_dog.speak())
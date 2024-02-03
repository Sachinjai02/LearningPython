class Dog:

    # Class object Attribute
    # Same for any instance of a class
    species = 'mammal'

    def __init__(self, breed, name, spots):
        self.breed = breed
        self.name = name
        self.spots = spots


    def bark(self, num_times):
        print("My name is {}".format(self.name))
        for n in range (1, num_times+1):
            print("WOOF WOOF!!!")

my_dog = Dog('Huskie', 'Charlie', False)
print(my_dog.spots)
print(my_dog.name)
print(my_dog.breed)
print(my_dog.species)
my_dog.species = 'hammal'

my_dog2 = Dog('Lab', 'Sammy', True)
print(my_dog2.spots)
print(my_dog2.name)
print(my_dog2.breed)
print(my_dog2.species)

print(my_dog.species)
my_dog.bark(2)
my_dog2.bark(3)
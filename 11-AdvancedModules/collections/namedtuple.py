from collections import namedtuple

normalTup = (10,20,30)
print(normalTup)
print(normalTup[2])

Dog = namedtuple('Dog',["age","breed","name"])
sammy = Dog(age = 5, name = 'Sam', breed = 'husky')
print(Dog)
print(sammy)

print(f'{sammy.age} should be same as {sammy[0]}')
print(f'{sammy.name} should be same as {sammy[2]}')
print(f'{sammy.breed} should be same as {sammy[1]}')
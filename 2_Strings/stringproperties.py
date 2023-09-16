#Immutability
name = 'Hello World'
print("Hey! " + name)

#name[0] = 'P' -- doesn't work
last_letters: str = name[1:]

newName = 'P' + last_letters
print("You are now changed to : " + newName)

#multiple concatenations at same time
print(10 * 'z')

print ('AB' * 4)

print(newName.capitalize())
print(newName.upper())
print(newName.lower())

print(name.split())

print("Hey! This is Sachin Jain".split('i'))

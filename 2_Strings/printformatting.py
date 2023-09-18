#String formatting
print("my name is {}. I am trying to learn {}".format('Sachin Jain', 'PYTHON!!!'))


print('The {0} {2} {1} {1}'.format('ZERO', "ONE", "TWO"))

print('The {z} {t} {one} {one}'.format(z='ZERO', one="ONE", t="TWO"))

result = 100/777

print("result is {r:22.10f}".format(r=result))
print("The result is {r:1.5f}".format(r=result))

name = "Sachin"
age = 30
#3.6 python; fstring syntax!!
print(f'Hello! {name}. You are {age} years old..')
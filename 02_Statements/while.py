x = 0
while x < 5:
    print(f'The current value of x is {x}')
    x = x + 1
else:
    print(f'while loop terminated. The current value of x is {x}')

x = [1,2,3]

for item in x:
    #comment alone would not work
    pass

mystring = 'Sachin'
for letter in mystring:
    if letter == 'a':
        continue
    elif letter == 'i':
        break
    else:
        print(letter)

print('end of my file')

list1 = [1, 2, 1, 4, 5, 1]

list1.append(6)

print(list1.count(1))

x = [1, 2, 3]
y = [4, 5, 6]

x.append(y)
print(x)

y.extend([7,8,9,10,11])
print(y)

print(y.index(8))

y.insert(5,34)
print(y)

el = y.pop()
print(f'{el} popped from {y}')
el = 9

y.remove(el)
print(f'{el} removed first instance from {y}')

y.reverse()
print(y)
y.sort()
print(y)
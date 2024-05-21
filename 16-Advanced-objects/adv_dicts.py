d = {'k1':1, 'k2':2}

# dictionary comprehension
mydict = { x:x**2 for x in range(10)}
print(mydict)

mydict = {k:v**2 for k,v in zip(['a','b'], range(2))}
print(mydict)

for k in d.keys():
    print(k)

for (k,v) in d.items():
    print(f'{k} and {v}')

dict1 = { k:k**3 for k in range(5)}
list1 = [k for k in range(5) if k%2 ==0]
print(dict1)
print(list1)
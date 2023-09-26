my_iterable = "hello"
for character in my_iterable:
    print(character)

my_iterable = [12,12,13,144]
for item in my_iterable:
    print(item)
sum = 0
for num in my_iterable:
    if num%2 == 0:
        print(f'{num} is even!')
    else:
        print(f'{num} is odd!!')
    sum += num

print(f'sum of all elements is {sum}')

for _ in [1,2,3,4,5,6,7,8,9,10]:
    print('I am cool!')

for tup in (1,2,3):
    print(tup)

##Tuple unpacking
tupList = [(1,2),(3,4),(5,6),(7,8)]
for (a,b) in tupList:
    print(a)
    print(b)

for a,b in tupList:
    print(a)

##iterating on dict
d  = {'k1':1,'k2':2,'k3':3}

##by default iteration on dict is keys; note dict are unordered
for k in d:
    print(k)
    print(d[k])

for k in d.keys():
    print(k)

for v in d.values():
    print(v)

for k,v in d.items():
    print(f'key {k}: value {v}')
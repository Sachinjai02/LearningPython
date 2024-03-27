from collections import defaultdict


d = {'a': 10}
print(d['a'])
#print(d['Wrong']) # Results in a KeyError

d = defaultdict(lambda: 0)
d['correct'] = 1000
print(d['correct'])
print(d['in-correct'])
print(d)
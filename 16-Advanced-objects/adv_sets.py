s = set()
s.add(1)
s.add(2)
s.add(2)

print(s)

s.clear()
print(f"set after clear() is {s}")
s.add(1)
sc = s.copy()
s.add(4)
sc.add(5)
print(f"Set and its copy are {s} and {sc}")

s = {1,2,3,4,5}
sc = {1, 2, 3, 4}
print(s.difference(sc))
print(s)
print(sc)
print(sc.difference(s))
s.difference_update(sc) # doesn't return anything just updates the first set after removing common elements
print(s)
print(sc)

s.discard(5)
print(s)

s1 = {1,2,3, 4}
s2 = {1, 2, 4}
print(s1.intersection(s2))

s1.intersection_update(s2)
print(s1)

s1 = {1, 2 , 3}
s2 = {1, 2}
s3 = {4, 5}
print(s1.isdisjoint(s2))
print(s1.isdisjoint(s3))

print(s2.issubset(s1))
print(s1.issuperset(s2))

s1 = {1, 2 , 3}
s2 = {1, 2}
print(s1.symmetric_difference(s2))
s1.symmetric_difference_update(s2)
print(s1)


s1 = {1, 2 , 3}
s2 = {1, 2, 4}

print(s1.union(s2))
s1.update(s2)
print(s1)

set1 = {2,3,1,5,6,8}
set2 = {3,1,7,5,6,8}
print(set1.difference(set2))
print(set2.union(set1))
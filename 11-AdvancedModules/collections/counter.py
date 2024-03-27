from collections import Counter
# Counter is a collection that's a sub class of dictionary

mylist = [1, 1, 1, 2, 3, 4, 2, 1, 2, 3, 4, 3, 2, 1, 1, 1]
counter = Counter(mylist)
print(counter)

mylist = ['a', 'b', 'c', 1, 1, 'a', 'a', 'a', 'b', 3, 3, 3, "hello"]
print(Counter(mylist))

sentence = "How many times does each word show up in this sentence with a word"
print(Counter(sentence.split()))

letters = 'aaabbbbbbbbcccccccccccccdddddd'
counter = Counter(letters)
print(counter)

# 3 most common occurring element in decreasing order in a tuple list
print(counter.most_common(3))


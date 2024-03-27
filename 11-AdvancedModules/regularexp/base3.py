import re

print(re.findall(r'cat|dog', 'The cats and dogs are here..'))

print(re.findall(r'.at', 'The cat in the hat sat there and it went splat.'))

# start with a number
print(re.findall(r'^\d','1 is a number'))

# ends with a number
print(re.findall(r'\d$','The number is 0'))

# get all things that are not numbers .. Grouping for exclusions
phrase = 'There are 3 numbers 34 inside 5 this sentence'

pattern = r'[^\d]+'
print(re.findall(pattern, phrase))

test_phrase = 'This is a string! Byt it has punctuation. How can we remove it?'
pattern = r'[^!.?]+'
clean = re.findall(pattern, test_phrase)
print(''.join(clean))

# Grouping for inclusions
test_phrase = 'Only find the hypen-words in this sentence. But you do not know how long-ish they are'
pattern = r'[\w]+-[\w]+'
clean = re.findall(pattern, test_phrase)
print(clean)

text = 'Hello this statement has catfish'
text2 = 'Hello this statement has catnap'
text3 = 'Hello this statement has caterpillar'
pattern = re.compile(r'cat(fish|nap|erpillar)')
print(re.search(pattern, text3))
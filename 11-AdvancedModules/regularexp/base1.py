import re

my_dog = 'I have a dog'
print(('dog' in my_dog))

text = 'My phone number is 123-456-7890. Call soon on my phone!'
pattern = 'phone'
match = re.search(pattern, text)
print(match.span())
print(match.start())
print(match.end())
print(match.group()) # matched string


matching_strings = re.findall(pattern, text)
print(matching_strings)

for match in re.finditer(pattern, text):
    print(match)

pattern = 'I am not present'
print(re.search(pattern, text))
import re
text = 'My phone number is 408-555-1234'
pattern = r'\d{3}-\d{3}-\d{4}'
phone = re.search(pattern, text)
print(phone)
print(phone.group())

text = 'plural'
pattern = r'plurals?'
print(re.search(pattern, text))

text = 'anycharacters'
pattern = r'\w{2,}'
print(re.search(pattern, text))

text = '123abc'
pattern = r'\d{2,4}'
print(re.search(pattern, text))

text = 'AAACC'
pattern = r'A*B*C*'
print(re.search(pattern, text))

text = 'Version A-b1_1.123'
pattern = r'Version \w-\w+.\w+'
print(re.search(pattern, text))

text = 'My phone number is 408-555-1234'
pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
phone = re.search(pattern, text)
print(phone)
print(phone.group())
print(phone.group(1))
print(phone.group(2))
print(phone.group(3))
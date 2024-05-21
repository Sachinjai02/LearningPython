s = 'hello world'
s = s.upper()
print(s)


s = s.lower()
print(s)


s = s.capitalize()
print(s)

print(f"count of o's in {s} = {s.count('o')}")
print(f"index of o in {s} = {s.find('o')}")

print(f'centering {s} between zeees : {s.center(20,"z")}')

print('hello\thi'.expandtabs())

print("helloSachin222".isalnum())
print("isSacgub".isalpha())
print("lower".islower())
print("   \t".isspace())
print("Title Letters Are Present 123".istitle())

s = 'hello examples'
print(s.split('e'))
print(s.partition('e'))

s = 'twywywtwywbwhsjhwuwshshwuwwwjdjdid'
print(s.count('w'))
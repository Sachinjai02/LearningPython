def simple_gen():
    for x in range(4):
        yield x


for number in simple_gen():
    print(number)


gen_obj = simple_gen()
print(gen_obj)

print(next(gen_obj))
print(next(gen_obj))
print(next(gen_obj))
print(next(gen_obj))
# print(next(gen_obj)): This will result into StopIteration error

s = "hello"
s_iterator = iter(s)
print(next(s_iterator))
print(next(s_iterator))
print(next(s_iterator))
print(next(s_iterator))
print(next(s_iterator))

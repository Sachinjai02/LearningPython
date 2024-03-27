def generate_fibonacci(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a,b = b, a+b


for a in generate_fibonacci(10):
    print(a)
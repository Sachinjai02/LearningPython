import timeit
import time

def func1(n):
    return [str(num) for num in range(n)]

def func2(n):
    return list(map(str, range(n)))

def func3(n):
    output = []
    for num in range(n):
        output.append(str(num))
    return output

time1 = time.time()
func1(10**6)
#print()
time2 = time.time()
print(f'Function1 took about {time2-time1} seconds')
func2(10**6)
#print(func2(10**6))
time3 = time.time()
print(f'Function2 took about {time3-time2} seconds')
func3(10**6)
time4 = time.time()
print(f'Function3 took about {time4-time3} seconds')


stmt = '''
func1(100)
'''
setup = '''
def func1(n):
    return [str(num) for num in range(n)]
'''
print(timeit.timeit(stmt,setup,number = 10**5))

stmt = '''
func2(100)
'''
setup = '''
def func2(n):
     return list(map(str, range(n)))
'''
print(timeit.timeit(stmt,setup,number = 10**5))
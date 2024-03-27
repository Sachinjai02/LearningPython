def create_cubes(n):
    for num in range(n):
        yield num**3


for cubes in create_cubes(10):
    print(cubes)
import random

#Each time it will run, it will provide a different random set of numbers
for i in range(10):
    print(random.randint(1, 10))

print("Producing random number with a seed of 101")
# The batch output will be same each time its run
random.seed(101)
for i in range(10):
    print(random.randint(0, 100))

print("Random numbers from the list")
mylist = list(range(0,20))
for i in range(10):
    print(random.choice(mylist))
print(mylist)

# SAMPLE WITH REPLACEMENT
print(random.choices(population=mylist, k=10))

# SAMPLE WITHOUT REPLACEMENT
print(random.sample(population=mylist, k=10))

print(mylist)
random.shuffle(mylist)
print(f"shuffled list: {mylist}")

# PROBABILITY DISTRIBUTION
print(random.uniform(a=0, b=100))
print(random.gauss(mu=0, sigma=1))

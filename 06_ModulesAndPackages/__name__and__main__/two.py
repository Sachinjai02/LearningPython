import one
from one import func

print("Top level in two.py....")

func()

# Python automatically assigns this reserved keyword __name__ a value "__main__" if this script has been run explicitly
if __name__ == '__main__':
    print("Two.py is run directly")
else:
    print("Two.py is imported")
# one.py

def func():
    print("Func() in one.py")


print("Top level in one.py")

# Python automatically assigns this reserved keyword __name__ a value "__main__" if this script has been run explicitly
if __name__ == "__main__":
    print('one.py is run directly')
else:
    print('one.py has been imported!')

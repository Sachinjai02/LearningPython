try:
    f = open('testfile', 'r')
    f.write('Writing a test line')
except TypeError:
    print("There is a type error!")
except OSError:
    print("OS Error occurred!")
except:
    print("All other errors!!! ")
finally:
    print("I always run!!!!")

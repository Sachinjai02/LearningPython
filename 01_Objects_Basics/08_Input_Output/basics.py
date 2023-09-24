myfile = open('test.txt')
print(myfile.read())
print(f'\nreading the file again')
print(myfile.read())

print(f'\nSeeking to 0 and reading the file again')
myfile.seek(0)
print(myfile.read())

myfile.seek(0)
print(f'\nSeeking to 0 and reading the file again with readLines')
print(myfile.readlines())

myfile.close()

###New way to handle file io -- it auto closes the file after finishing this statement execution
with open('test.txt') as myfile:
    contents = myfile.read()
    print(contents)

####Write operations..
with open('test2.txt',mode='r') as myfile:
    print(myfile.read())

with open('test2.txt',mode='a') as myfile:
    myfile.write("\nWriting a new line to my new file!!!")

with open('test2.txt',mode='r') as myfile:
    print(myfile.read())

with open('test3.txt',mode='w') as myfile:
    myfile.write("\nWriting a new line to my new file!!!")

print('reading file created by w mode')
with open('test3.txt',mode='r') as myfile:
    print(myfile.read())
import os
import shutil
import send2trash

f = open('practice.txt', 'w+')
f.write("This is a test string")
f.close()

pwd = os.getcwd()
print(f'Current directory is {pwd}')

print(f'Items in current directory is: {os.listdir()}')

print(f'Items in /Users/sachinja/PycharmProjects directory is: {os.listdir("/Users/sachinja/PycharmProjects")}')
shutil.move('practice.txt', './new_directory/practice.txt')

# os.unlink(path) -- remive a file
# os.rmdir(path) -- remove a folder (but it should be empty)
# shutil.rmtree(path) -- remove all files and folders contained in the path
# All of above are irrecoverable deletes i.e. we would not be able to recover deleted files/folders

shutil.move('./new_directory/practice.txt', './practice.txt')
send2trash.send2trash('practice.txt')
# As the name suggests this would put files/folders into trash bins

for folder, sub_folders, files in os.walk('/Users/sachinja/PycharmProjects/LearningPython/11-AdvancedModules'):
    print(f"Current looking at {folder}")
    print("\n")
    print('The sub_folders are:')
    for sf in sub_folders:
        print(f"\t Subfolder:{sf}")
    print("\n")
    print('The files are:')
    for f in files:
        print(f"\t File:{f}")
    print("\n")

"""Import Modules and Exploring The Standard Library"""

import sys
import os

# first value because this is added first
# if a module is in a different folder, manually add directory to sys.path
sys.path.append('location_of_module')
print(sys.path)
# or add on mac export PYTHONPATH="modules_path_to_add"

# look into os module
current = os.getcwd()

print(os.getcwd())

# go to new location
# os.chdir('/Users/gonzalo/Documents/GitHub/Learning_Central')
# print(os.getcwd())

# list all files
print(os.listdir())

# makedirs --> create nested directors, makedir --> creates one level directory
# os.makedirs('test')
os.makedirs('test1/test2')
os.removedirs('test1/test2')

# rename
# os.rename("test.txt", "test2.txt")

print(os.stat('test2.txt'))
print(os.stat('test2.txt').st_mtime) # I can create the time using the timestamp

# generator as it walks the directory and yields some things. traverses top down
# three value tuple
for (dirpath, dirname, filenames) in os.walk(os.getcwd()):
  print('All')
  print(dirpath)
  print(dirname)
  print(filenames)

# print(os.environ)

print(os.environ.get('HOME'))
# create a file path
# file_path = os.path.join(os.environ.get('HOME'), 'some_file.txt')
# print(file_path)

# # getting base, dirname or both 
# print(os.path.basename('/tmp/test.txt'))
# print(os.path.dirname('/tmp/test.txt'))
# print(os.path.split('/tmp/test.txt'))

# # get the extension of a file
# print(os.path.splitext('/tmp/test.txt'))

# Files: default is reading
# f = open('text.txt', 'r')
# print(f.name)
# for line in f:
#   print(line.rstrip())
# f.close()

# use a context manager, once I exit the block file would be closed. File is also closed if an error is thrown
with open('text.txt', 'r') as fl:
  for line in fl:
    print(line, end="")
    # print(fl.read())
    # f_contents = fl.read()
    # f_contents = fl.read(100)  # reads the first 100 characters
    # f_contents = fl.readlines()
    # f_contents = fl.readline()
    # print(f_contents, end="")

with open('test3.txt', 'w') as f:
  f.write('what')
  f.write('is this?')

with open('test2.txt', 'r') as rf:
  with open('test3.txt', 'w') as wf:
    for line in rf:
      wf.write(line)


# open images in byte arrays to copy binary code, open('test2.txt', 'rb or wb') 
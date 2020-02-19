from collections import namedtuple

t = (1, 2, 3)
print(t[0])

# named tuple assigns a name and value
# creates a class Dog
# pass in name of class and string with various attributes of class
Dog = namedtuple("Dog", "age breed name")
sam = Dog(age=2, breed="lab", name="sammy")
print(sam.age)


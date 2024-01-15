# Refresher 

# integer division 
ans = 64 // 10

# mod gives the remainder
ans_mod = 64 % 10
# regular division
ans_division = 64 / 10

# inputs always return a string

"""
Conditions
<, >, == !=
"""

name = "Alison"
print(name != "alison")

"""
if-elif-else

making decisions based on some condition

"""
condition = 10
if 10 <= condition:
  print('Yes it is')
  
  
"""
Chained Conditionals & Nested Statements
adding multiple conditions in one line
if something and something or

not(condition) --> reverses the condition
"""


"""
For Loops
for n in array:
  print(n)
  
range(start, stop, step)
"""
for n in range(10):
  print(n, end=", ")


"""
While Loops
"""
"""
List's and Tuples
"""
"""
Iteration by Item
"""

# inpt = input('Something: ')
# print(inpt.strip())

"""
String Methods
"""
"""
Slice Operator
"""
"""
Functions
"""

def func_name():
  pass

"""
How to Read a Text File

- have the file in the same directory to avoid path joining else I will need to create a path to the file
- new line characters are created.
"""

someFile = open('test.txt', 'r')

readLines = someFile.readlines()

newList = []
for line in readLines:
  newList.append(line.strip())
  # newList.append(line[:-1])
# print(readLines)
print(newList)

someFile.close()

"""
Writing to a Text File
- append or write
"""
writeToThis = open('test.txt', 'a')

writeToThis.write('Python3\n')
writeToThis.close()

"""
Using .count() and .find()
if it does not find it, it will return -1
"""
str = "GOnzalo"
# finds the first l
print(str.find('l'))

"""
Introduction to Modular Programming
modules and imports
can be built int or user defined

"""
from typing import Any
import myModule
print(myModule.funOne(4))
print(myModule.funTwo(10))

"""
Optional Parameters
- can have multiple parameters
- can have default parameters
"""
def func(x=3, text=2):
  print(x)
  if text == '1':
    print('is 1')
  else:
    print('not 1')

func('3', '1')

"""
Try and Except (Error Handling)
"""
# validate text from user inout
# text = input('Username: ')
# text = 'hey'
text = '234'
try:
  number = int(text)
  print(number)
except:
  # what I want to do if there is an error
  print('Invalid username. Only contain numbers')
  
"""
Global vs Local Variables
"""
# var is a global variable any method can access this
var = 9
loop = True
newVar = 100

def funcThis(x):
  # newVar is a local variable to funcThis and can nly be accessed here
  # this variable will be used when printing newVar
  newVar = 7
  # access a global variable
  global loop
  loop = 7
  
  if x == 5:
    return newVar

funcThis(6)
print(loop)

"""
📗 Object Oriented Programming 📗
"""

"""
Introduction to Objects
- in python an object is pretty much anything
"""

x = 10
y = 'string'

print(type(x))
print(type(y))

"""
Creating Classes
"""
# 
class Dog(object):
  
  # constructor is called when we create a new object of type Dog
  # can include as many parameters as I need
  def __init__(self, name, age):
    # self refers to the instance object being created. Similar to the this keyword
    print('Constructor called: Made a Dog')
    # create attributes similar to fields
    self.name = name
    self.age = age
    self.li = [1,3,4]
  
  # self is used here to
  def speak(self):
    print(f'Hi I am {self.name} and I am {self.age} years old')
  
  def talks(self):
    print(f'Bark Bark')
  
  def change_age(self, age):
    self.age = age
  
  # I can create more attributes later or set self.weight to null
  def add_weight(self, weight):
    self.weight = weight

me = Dog('Fred', 18)
mike = Dog('Mike', 10)
me.change_age(16)
me.speak()
mike.speak()

# I can access the attributes from the object but I should not do this. use getters and setters
print(me.age)



"""
Inheritance
"""
class Cat(Dog):
  
  def __init__(self, name, age, color):
    # inherit all attributes and methods of Dog
    # calls the Dog constructor method of the super class, parent class
    super().__init__(name, age)
    self.color = color
  
  def talk(self):
    print(f'Meow meow')

cat = Cat('Cat', 12, 'blue')
cat.speak()
cat.talk()


class Vehicle():
  
  def __init__(self, price, gas, color) -> None:
    self.price = price
    self.gas = gas
    self.color = color
  
  def fillUpTank(self):
    self.gas = 100
  
  def emptyTank(self):
    self.gas = 0
  
  def gasLeft(self):
    return self.gas


class Car(Vehicle):
  
  def __init__(self, price, gas, color, speed) -> None:
    super().__init__(price, gas, color)
    self.speed = speed
  
  def beep(self):
    print(f'Beep Beep')

class Truck(Car):
  def __init__(self, price, gas, color, speed, tires) -> None:
    super().__init__(price, gas, color)
    self.speed = speed
    self.tires = tires
  
  def beep(self):
    print(f'Honk Honk')
    
"""
Overloading Methods
"""
"""
Static Methods and Class Methods
"""
"""
Private and Public Classes
"""
"""

📘 Intermediate Python 📘
"""
"""
Optional Parameters
"""
def func(word, x=1):
  return word * 2

call = func("Jim", 5)
print(call)

"""
Static and Class Methods
- good way to organize things
"""
class Person(object):
  # class variable can be accessed by the class not the instance
  population = 50
  
  def __init__(self, name, age):
    self.name = name
    self.age = age

  # Call from Class not instance
  @classmethod
  def getPopulation(cls):
    return cls.population
    
  def isAdult(age):
    return age >= 18
  
  # can be called on any class instance
  @staticmethod
  def display(self):
    print(f'{self.name} is {self.age} years old')


newPerson = Person('Alexa', 18)
print(Person.getPopulation())
print(Person.isAdult(90))

"""
Map Function
- apply a function to a list (all iterables) and create new values
- I can use a for loop pr map
"""
li = [1,2,3,4,5,6,7,8,9,10]

def func2(x):
  return x**x

# map accepts a function and a list
# map will apply the function to all items of the list
print(list(map(func2, li)))

# list comprehension
print([func2(x) for x in li if x % 2 == 0])

"""
Filter Function
- filter for items and add them to a list
"""

def add7(x):
  return x + 7

def isOdd(x):
  return x % 2 != 0

a = [1,2,3,4,5,6,7,8,9,10]

# filter returns all of the values that are true
b = list(filter(isOdd, a))
print(b)

c = list(map(add7, b))
print(c)
"""
Lambda Function
- anonymous function 
"""
def func3(x):
  return x + 5

print(func3(10))

func4 = lambda x: x + 5
print(func4(10))

def funcL(x):
  func44 = lambda x: x + 5
  return func44(x)

print(funcL(10))

alist = [1,2,3,4,5,6,7,8,9,10]
newList2 = list(map(lambda x: x + 5, alist))
print(newList2)

"""
Introduction to Collections
Containers
- list
- set
- dict
- tuple

Types
- counter
- deque
- namedTuple
- orderdDict
- defaultdict

- intersection --> minimum elements in each list
- union --> max elements in each counter
- 

"""
import collections
from collections import Counter

c = Counter('gallad')
c2 = Counter(['a', 'b', 'c', 'c', 'a'])
c3 = Counter({'a': 1, 'c': 7, 'b': 2})
c4 = Counter(cats=4, dogs=7)
print(c)
print(c2)
print(c3)
print(c4)
print(c4['cats'])

print(list(c.elements()))
print(list(c3.elements()))
print(c.most_common(2))

c5 = Counter(a=4, b=2, c=0, d=-2)
d = ['a', 'b', 'b', 'c']
c5.subtract(d)
print(c5)

"""
Named Tuple
- access field by names instead of index difference between tuple and named tuples
"""
from collections import namedtuple

# automatically breaks up string into three parameters
# any iterable object works as a parameter
Point = namedtuple('Point', 'x y z')
newP = Point(3,4,5)
print(newP)
print(newP._fields)


"""
Deque
- Looks like a list
- faster when adding to end and beginning of a list
- random access use a list not a deque
- for more methods look at dir(d)
- or look over documentation
- use extend to add multiple items to the deque
"""
from collections import deque
d = deque("hello")
print(d)
d.append('4')
d.append(5)
d.appendleft(3)
print(d)
d2 = deque("the", maxlen=3)
print(d2)
d2.appendleft("d")
print(d2)

"""
📙 Advanced Python 📙
- error will not be shown at compile time only run time
- most items in python are objects
"""

class DogTwo:
  
  def __init__(self):
    self.bark()

# dogTwo = DogTwo()

def make_class(x):
  class DogThree:
    def __init__(self, name):
      self.name = name
    
    def print_value(self):
      print(x)
  
  # return is the class itself which is a reference to the class
  return DogThree

# return the class not an instance
# things are being stored in memory when we define something
# so we can interact with them live
# <class '__main__.make_class.<locals>.DogThree'> .... locals is what is inside the class
clsOne = make_class(x)
print(clsOne)
dd = clsOne("name")
print(dd.name)
dd.print_value()

for i in range(10):
  def show():
    print(i*2)
  show()

"""
Overview of Python
"""
def func22(x):
  if x == 1:
    def rv():
      print(f'X is = 1')
  else:
    def rv():
      print(f'X is not = 1')
  return rv

new_func = func22(1)
new_func()

print(id(new_func))

# Inspecting objects
import inspect
from queue import Queue

print(inspect.getmembers(new_func))
print(inspect.getsource(new_func))
print(inspect.getsource(Queue))

"""
Dunder/Magic Methods
- 
"""
x = [1,2,3]
b = [4, 5]
print(x + b)
print(x * 3)

class Person:
  
  def __init__(self, name):
    self.name = name

  # Dunder methods or data model methods
  def __repr__(self) -> str:
    return f"Person({self.name})"
  
  def __mul__(self, x):
    if type(x) is not int:
      raise Exception("Invalid argument")
    self.name = self.name * x
  
  def __call__(self, y):
    print(f'Called this function: {y}')
    
  def __len__(self): 
    return len(self.name)
    
p = Person('Alexa')
p*4
print(p)
p(4)
print(len(p))

from queue import Queue as q

class Queue2(q):
  
  def __repr__(self):
    return f'Queue({self._qsize()})'

qq= Queue2()
print(qq)

"""
Metaclasses
- how classes are instantiated / created
- classes are objects
- interact with it at runtime
- classes also create objects for us - 
- there is a high level instance that creates a class object

- Few instances when metaclass is needed
- defines the rules for a class, how it is created
- 
"""

class Foo:
  def show(self):
    print('HI!!')

def add_attribute(self):
  self.z = 9
  
Test = type('Test', (Foo,), {"x":5, "add_attribute": add_attribute}) # Creates the class: name, inherits from parent class, attributes
print(Test)
print(type(Test)) #meta class, calls a type constructor
print(Test())
t = Test()
t.wy = "Hello"
t.add_attribute()
print(t.x)
print(t.wy)
t.show()
print(t.z)

# inherit from type
#  Meta class can inherit from another Meta class
class Meta(type):
  # before init method
  def __new__(self, class_name, bases, attrs):
    print(f'{class_name} - {bases} - {attrs}')
    a = {}
    for name, value in attrs.items():
      if name.startswith("__"):
        a[name] = value
      else:
        a[name.upper()] = value
    print(f'{a}')
    return type(class_name, bases, a)
    

class Dogg(metaclass=Meta):
  x = 5
  y = 8 

  def hello(self):
    print('HI')

d = Dogg()
print(d.X)

"""
Decorators
- useful to validate user input
- logging function calls
- keeping track of time it takes to run code
- debugging
"""

def func10(string):
  def wrapper():
    print("Started")
    print(string)
    print("Ended")
  return wrapper

def func12(f):
  def wrapper():
    print("Started")
    f()
    print("Ended")
  return wrapper

def func11():
  print("Func 11")
  
def func13():
  print("func 13")
  
x = func10("Hello")
print(x)
x()

x2 = func12(func11)
y2 = func12(func13)
print(x2)
x2()
y2()

print("-------------")
# to avoid calling func12 then call function do
func11 = func12(func11)
func13 = func12(func13)
func11()
func13()

print("What the decorator does")

def funcDec(f):
  # we don't know how many arguments are 
  # positional or keyword arguments
  def wrapper(*args, **kwargs):
    print("Started")
    rv = f(*args, **kwargs)
    print("Ended")
    return rv
  return wrapper

@funcDec
def funcWithDecorator(x, y):
  print(f'Func with Decorator {x}')
  return y

@funcDec
def funcWithNoParams():
  print("Func with Decorator no params")

# the wrapper will also need the same number of parameters that I am passing to the function
funcWithDecorator(4, 7)
# make sure that the value of the function in the wrapper is returned
ret = funcWithDecorator(5, 8)
print(ret)

import time
def timer(f):
  def wrapper(*ars, **kwargs):
    start = time.time()
    rv = f()
    total = time.time() - start
    print(f'Time {total}')
    return rv
  return wrapper

@timer
def test():
  for _ in range(10000):
    pass

test()

"""
Generators
- we are limited to the amount of ram in our computers because we store everything in memory
- the yield keyword returns the value and pauses the function 
- we keep track of n and all internal information stored in memory
"""

# x = [i**2 for i in range(1000000000000)]

# for el in x:
#   print(x)

# for i in range(100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000):
#   print(i)

class Gen:
  def __init__(self, n):
    self.n = n
    self.last = 0
    
  def __next__(self):
    return self.next()
  
  def next(self):
    if self.last == self.n:
      raise StopIteration()
    
    rv = self.last ** 2
    self.last += 1
    
    return rv
  
g = Gen(100)  

# while True:
#   try:
#     print(g.next())
#   except StopIteration:
#     break  


def gen(n):
  # the yield keyword returns the value and pauses the function
  #  we keep track of n and all internal information stored in memory
  for i in range(n):
    yield i**2

import sys
g = gen(100)
# for i in g:
#   print(i)

x = [1 ** 2 for i in range(100)]

print(f'size of g in memory: {sys.getsizeof(x)}')
print(f'size of g in memory: {sys.getsizeof(g)}')
    
"""""
Context Managers
- 
"""
#  this works but something easier is context manager
try:
  file = open('file.txt', 'w')
  # if something happens here we need to make sure to close the file
  #  how can we make sure we close the file: try 
  file.write('What')
finally: 
  file.close()
  
# with keyword to open file with context manager
with open("file.txt", "w") as file:
  file.write("Hey")
  

class File: 
  
  def __init__(self, filename, method):
    self.file = open(filename, method)
  
  def __enter__(self):
    # return some value to use in context manager
    print("Enter")
    return self.file
  
  # params are called if there is an exception
  def __exit__(self, type, value, traceback):
    print(f'{type}, {value}, {traceback}')
    print("Exit")
    self.file.close()
    # if True is returned we are telling python Exception is fine
    if type == FileExistsError:
      return True
    else:
      return False
    
with File("file.txt", "w") as f:
  print("Middle")
  f.write("hey hey")
  # handle exception in __exit__
  # raise FileExistsError("Failed on purpose")


print("----------- do the same things -------------")
from contextlib import contextmanager

@contextmanager
def filename(filename, method):
  print("enter")
  file = open(filename, method)
  yield file
  file.close()
  print("Exit")
  
with filename('text.txt', 'w') as f:
  print("middle")
  f.write("Hello")


# Refresher 

# integer division 
ans = 64 // 10

# mod gives the remainder
ans_mod = 64 % 10
# regular division
ans_division = 64 / 10

# inputs always return a string

"""
(00:24:11) Conditions
<, >, == !=
"""

name = "Alison"
print(name != "alison")

"""
(00:32:54) if-elif-else

making decisions based on some condition

"""
condition = 10
if 10 <= condition:
  print('Yes it is')
  
  
"""
(00:45:56) Chained Conditionals & Nested Statements
adding multiple conditions in one line
if something and something or

not(condition) --> reverses the condition
"""


"""
(00:53:29) For Loops
for n in array:
  print(n)
  
range(start, stop, step)
"""
for n in range(0, 10, 2):
  print(n, end=", ")


"""
(00:59:29) While Loops
"""
"""
(01:05:51) List's and Tuples
"""
"""
(01:14:09) Iteration by Item
"""

# inpt = input('Something: ')
# print(inpt.strip())

"""
(01:20:13) String Methods
"""
"""
(01:26:38) Slice Operator
"""
"""
(01:33:41) Functions
"""

def func_name():
  pass

"""
(01:42:10) How to Read a Text File

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
(01:50:31) Writing to a Text File
- append or write
"""
writeToThis = open('test.txt', 'a')

writeToThis.write('Python3\n')
writeToThis.close()

"""
(01:54:50) Using .count() and .find()
if it does not find it, it will return -1
"""
str = "GOnzalo"
# finds the first l
print(str.find('l'))

"""
(02:01:47) Introduction to Modular Programming
modules and imports
can be built int or user defined

"""
import myModule
print(myModule.funOne(4))
print(myModule.funTwo(10))

"""
(02:09:28) Optional Parameters
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
(02:15:36) Try and Except (Error Handling)
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
(02:20:29) Global vs Local Variables
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
(02:29:16) Introduction to Objects
- in python an object is pretty much anything
"""

x = 10
y = 'string'

print(type(x))
print(type(y))

"""
(02:39:02) Creating Classes
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
(02:50:37) Inheritance
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
(03:03:13) Overloading Methods
"""
"""
(03:16:01) Static Methods and Class Methods
"""
"""
(03:25:44) Private and Public Classes
"""
"""

📘 Intermediate Python 📘
"""
"""
(03:31:40) Optional Parameters
"""
"""
(03:41:13) Static and Class Methods
"""
"""
(03:50:24) Map Function
"""
"""
(03:56:15) Filter Function
"""
"""
(04:03:12) Lambda Function
"""
"""
(04:10:12) Introduction to Collections
"""
"""
(04:22:17) Named Tuple
"""
"""
(04:30:20) Deque
"""
"""

📙 Advanced Python 📙
"""
"""
(04:40:12) Overview of Python
"""
"""
(04:58:34) Dunder/Magic Methods
"""
"""
(05:12:23) Metaclasses
"""
"""
(05:34:10) Decorators
"""
"""
(05:50:29) Generators
"""
"""
(06:04:32) Context Managers
"""
"""
Is any anonymous function
lambda arguments : expression

can have any number of arguments but only one expression

Use lambda functions when an anonymous function is required for a short period of time.
"""


add10 = lambda a: a + 10

# print(add10(5))

x = lambda a, b: a * b

# print(x(2,10))

def myfunc(n):
    return lambda a : a * n 

num = myfunc(2)
print(num(4))

arr1 = [1,2,3,4]
print(arr1)

arr1_copy = arr1.copy()
print(arr1_copy)

arr1_copy.append(5)
print(arr1_copy)
print(arr1)


class Person(object):

    def __init__(self, fname, lname=""):
        self.lname = lname
        self.fname = fname
    

    def change_lname(self, new_name):
        self.lname = new_name
    
    def print_name(self):
        return self.fname + " " + self.lname

class Student(Person):

    def __init__(self, fname, lname, schoolName):
        # Person.__init__(self, fname, lname)
        super().__init__(fname, lname)

        self.schoolName = schoolName   

    def print_name(self):
        return super().print_name() + " " + self.schoolName

# p1 = Person("John", "Smith")
# print(p1.print_name())
# p1.change_lname("Doe")
# print(p1.print_name())

# # p1.lname = ""
# # print(p1.print_name())

# s1 = Student("Jake", "Wrong", "RHS")
# print("From Student: " + s1.print_name())
# print(s1.lname)

## map function maps a function to each element in an iterable object
def square(num):
    return num**2

my_nums = [1,2,3,4,5, 10]

nums_squared = list(map(square, my_nums))
nums_lambda = list(map(lambda a: a**2, my_nums))
print((nums_lambda))

# Filters for true or false

def check_even(num):
    return num % 2 == 0

print(list(filter(check_even, my_nums)))
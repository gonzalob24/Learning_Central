import math
import random

# Iterators contain a countable number of values. 
# Allows me to traverse through all of the items.
# range() uses an iterator
# we can transform iterator to a list

# print(list(range(10)))

aTuple = ("one", "two", "three")

# iter_tuple = iter(aTuple)
# print(next(iter_tuple))
# print(next(iter_tuple))

for item in aTuple:
    print(item)

name = 'Gonzalo'
iter_name = iter(name)

print(next(iter_name))
print(next(iter_name))

################################
#####  CREATE AN ITERATPR   ####
################################

# Implement __iter__() and __next__() to object/class
# must always return self when using __iter__()
# __next__() return the next object in the sequence

class MyNumbers():

    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

numbers = MyNumbers()
# iter_numbers = iter(numbers)
# print(next(iter_numbers))
# print(next(iter_numbers))

for num in numbers:
    print(num)


def create_cubes(n):
    result = []

    for x in range(n):
        result.append(x ** 3)

    return result


c1 = create_cubes(10)  # Entire list is in memory
# we dont need it all in memory we can yield it instead of storing it in memory
print(c1)

for x in create_cubes(10):
    print(x)
print("\n\n")


# This method is more efficient b/c it does not store the list
# in memory it yields the values
# Generates the values as I need them.
def create_cubes2(n):
    result = []

    for x in range(n):
        yield (x ** 3)


# I get back the same results as before
for x in create_cubes2(10):
    print(x)


# fib sequence
# 1, 1, 2, 3, 5, 8, 13, 21..etc
def generate_fib(n):
    a = 1
    b = 1

    for i in range(n):
        yield a
        a, b = b, a + b


def generator_squares(n):
    """
    generator that generates the squares of numbers up to some number N.
    :return:
    """
    for x in range(n):
        yield x ** 2


def rand_numbers(n, low, high):
    for x in range(n):
        yield random.randint(low, high)


print("\n\nFib sequence:")

for number in generate_fib(10):
    print(number, end=" ")


# next and iter function

def simple_generator():
    for x in range(3):
        yield x


for number in simple_generator():
    print(number)

print("\n\nSimple Generator using next:")
g = simple_generator()

print(next(g))
print(next(g))
print(next(g))

s = "hello"  # String are iterable
# print(next(s)) s is not an iter
s_iter = iter(s)
print(next(s_iter))
print("\n\nSquare Generators:")
for number in generator_squares(10):
    print(number, end=" ")

print("\n\nRandom numbers generator:")

for number in rand_numbers(10, 1, 30):
    print(number, end=" ")

print("\n\nGenComp:")
my_list = [1, 2, 3, 4, 5]
gencomp = (item for item in my_list if item > 3)

for item in gencomp:
    print(item)

"""
  3 - Integers and Floats
"""

a = "ban"
b = "ban"

print(a is b)
print(a == b)

lst = [1,2,3,4]
del lst[0:2]
print(lst)

lst.sort(reverse=True)
print(lst)
print(sum(lst))
print(max(lst))

tup_1 = ('Hist', 'Mat', 'Sci')

set_1 = {'Hist', 'Math', 'Sci', 'Hist'}

set_2= {'Art', 'Math', 'Sci', 'Hist'}


print(set_1)
print('Hist' in set_1)

print(set_1.intersection(set_2))

# 
empty_list = []
empty_list = list()

empty_tuple = ()
empty_tuple = tuple()

# empty_set = {} # this wont work as this creates a dictionary
empty_set = set()

# Dictionary - map - Key, Value
# are mutable
# pop removes pair
student = {'name': 'Maria', 'age': 25, 'courses': ['BIOL', 'Math']}
print(student['name'])

import fib
print(fib.__name__)
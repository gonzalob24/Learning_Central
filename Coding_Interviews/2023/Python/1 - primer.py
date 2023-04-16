from testexport import add
from testexport import sumOfAllOddIntsSmallerThanN

test = 98.6

print(test)

# cast values to int or floats
print(float(4))
print(int(3.87))

# Lists
print(list('hello'))

# dict
pairs = [( 'ga' , 'Irish' ), ( 'de' , 'German' )]
print(dict(pairs))

print(3*'t')

a1 = [1, 2]
a2 = a1
print(a1 is a2)
print(a2 == a1)

a2 += [3, 4]
print(a1 is a2)

print(a1)
print(a2)

# this crates a new array and adds a reference to a3
a3 = a1 + [6, 7, 8]
print(a2 == a3)

# Print
print('a', 'b', 'c', sep=':')

# Files
# fb = open('file_name', 'mode_r_w_a: read, write, append')

# Raising a type error
# raise TypeError("Not a number")

print(add(1,9))
print(sumOfAllOddIntsSmallerThanN(5))
# this are just some examples of a few problems from the book.
import math

julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")

# print(julia[2])

b = ("Bob", 19, "CS")

(name, age, major) = b

# print(name)


def f(r):
    '''returns the (circ, area) of a circle '''
    c = 2 * math.pi * r
    a = math.pi * r * r
    return (c, a)


print(f(6))

word = "banana"

new_word = word.split()

d = dict()
d['csev'] = 2
d['cwen'] = 4

print(d.items())

for (k, v) in d.items():
    print(k, v)
# we can use sorted(d.items()) with a dictionary

c = {'a': 10, 'b': 22, 'd': 3, 'g': 11, 'c': 4, 'f': 40}
temp = list()
for (k, v) in c.items():
    temp.append((v, k))
print(sorted(c.items()))
print(temp)
print(sorted(temp))

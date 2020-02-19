# remembers order in which items are added
from collections import OrderedDict

d1 = {}
d1['a'] = 1
d1['b'] = 2

d2 = {}
d2['b'] = 2
d2['a'] = 1

print(d1 == d2)

d1 = OrderedDict()
d1['a'] = 1
d1['b'] = 2

d2 = OrderedDict()
d2['b'] = 2
d2['a'] = 1

# The reason its false its because
# They were added in a different order.
print(d1 == d2)

for k, v in d1.items():
    print(k, v)
print("\n\n")
d = OrderedDict()

d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
d['e'] = 5

for k, v in d.items():
    print(k, v)

print("\n\nCreating k,v using comprehension")

print({x: x ** 3 for x in range(5)})

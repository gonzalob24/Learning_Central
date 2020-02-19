# Numbers

print(hex(10))
print(bin(8))
print(pow(2, 3, 2))  # Third argument is treated as mod
print(abs(-99))
print(round(3.141592, 2))

# Strings
s = 'hello world'
print(s.capitalize())
print(s.upper())
print(s.count('o'))
print(s.find('o'))
print(s.rfind('o'))
print(s.center(20, 'z'))
# parsing through text data
print("hello\thi".expandtabs(tabsize=5))
ss = 'hello'
print(ss.isalpha())
print(ss.isalnum())
print(ss.islower())
print(ss.isspace())
print(ss.istitle())  # True is ss is a title case string
print(ss.isupper())
print(ss.endswith('o'))

print(ss.split('e'))
print(ss.partition('e'))  # returns the e (separater) as well

s2 = 'hiihhiiihhhhi'

print(s2.partition('i'))  # first instance only

"""
Sets used when comparing values
"""
print("\n\nSets:")
set1 = {2, 3, 1, 5, 6, 8}
set2 = {3, 1, 7, 5, 6, 8}

print("Elements in set1 not in set2: ",set1.difference(set2))
print("Elements in set1 and set2: ", set1.union(set2))

s = set()
s.add(1)
s.add(2)
s.add(3)
print(s)
sc = s.copy()
# s.clear()
print(s)
print(sc)
# Difference method returns the elements that are different
sc.add(4)
print(sc.difference(s))
print(s)
print(sc)

# returns set1 after removing all the elements found in set2
s1 = {1, 2, 3, 6}
s2 = {1, 4, 5}

s1.difference_update(s2)
print(s1)
s.discard(6)
print(s)

# Intersection of two or more sets, common to all sets

s1 = {1, 2, 3, 4}
s2 = {1, 2, 4}

print("Intersection: ", s1.intersection(s2))
s1.intersection_update(s2)  # changes / updates s1 to the intersection
print(s1)

s1 = {1, 2}
s2 = {1, 2, 4}
s3 = {5}

# returns true if they have a null intersection
print(s1.isdisjoint(s2))
print(s1.isdisjoint(s3))
print(s1.issubset(s2))
print(s2.issuperset(s1))

# Symmetric difference
print(s1.symmetric_difference(s2))

# Union returns the union of two sets, items in either set
print(s1.union(s2))
s1.update(s2)
print(s1)

"""
Dictionaries
"""
d = {'k1': 1, 'k2': 2}
# Creating defaulr k,v
print({k: v ** 2 for k, v in zip(['a', 'b'], range(2))})

# iterating over keys, value, items
print("\nPrintng k, v")
for k in d.items():
    print(k)

print("\nPrintng values")
for v in d.values():
    print(v)

print("\nPrintig keys")
for k in d.keys():
    print(k)
print("\n")

"""
Lists
"""

l = [1, 2, 3, 3]
l.append(4)
print(l)
print(l.count(10))
# Extend will extend the list instead of adding a list to an index
x = [1, 2, 3]
# x.append([4, 5])
print(x)
print(x.extend([4, 5]))
print(x)
print(l.index(2))
l.insert(2, "inserted")
l.insert(2, "inserted")
print(l)
print(l.pop())
print(l)
l.remove('inserted')
print(l)
l.reverse()
print(l)

l2 = [3, 6, 8, 1, 7]

l2.reverse()
print(l2)
l2.sort()
print(l2)

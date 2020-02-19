# Counter could be useful for natural language processing techniques

from collections import Counter

l = [1, 1, 1, 1, 1, 12, 2, 2, 2, 2, 2, 23, 3, 3, 34, 4, 4, 4, 5, 5, 5, 5]
print(Counter(l))


s = "aaasssdddfffgggasdnhd"
print(Counter(s))

s2 = "How many times does each word show up in this sentence word word shoe shoe up up up no no no"
s2 = s2.split()
print(Counter(s2))

c = Counter(s2)
print("Most Common: ",c.most_common(2))

# Common patterns when using the Counter() object
print("\nTotal words: ", sum(c.values()))  # total of all counts
# c.clear()             # resets all counts
print("\nList Unique: \n",list(c))     # list unique elements
print("\nSet: \n",set(c))           # Converts to a set
print("\nDictionary: \n",dict(c))          # converts to a regular dictionary
list_of_pairs = c.items() # convert to a list of (element, cnt) pairs
print("\nConverts from list (element, cnt) pairs: \n", Counter(dict(list_of_pairs)))  # Converts from a list of (elem, cnt) pairs
print("\nLeast Common: \n", c.most_common()[:-0-1:-1])     # n least common elements
c += Counter()          # remove zero and negative counts

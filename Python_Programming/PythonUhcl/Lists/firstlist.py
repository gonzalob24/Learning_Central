vocabulary = ["apple", "cheese", "dog"]
numbers = [17, 123]
an_empty_list = []

print(vocabulary, numbers, an_empty_list)
print(vocabulary[2 - 1])

students = [
    ("John", ["CompSci", "Physics"]),
    ("Vusi", ["Maths", "CompSci", "Stats"]),
    ("Jess", ["CompSci", "Accounting", "Economics", "Management"]),
    ("Sarah", ["InfSys", "Accounting", "Economics", "CommLaw"]),
    ("Zuki", ["Sociology", "Economics", "Law", "Stats", "Music"])]

print(len(students))
counter = 0
for (name, subjects) in students:
    if "CompSci" in subjects:
        counter += 1
        print(name)
print(counter)

a = "banana"
b = "banana"
print("length of a string")
print(len(a))

print(len(a))
print(a is b)
print(a == b)

a2 = [1, 2, 3]
b2 = a2

print(b2)
print(a2 is b2, a2 == b2)

b2[2] = 10

print("a2 is " + str(a2))
print("b2 is " + str(b2))

a3 = [4, 5, 6]
b3 = a3[:]

print(a3)
print(b3)

b3[0] = 100
print("a3 is")
print(a3)
print(b3)

xs = [1, 2, 3, 4, 5]
print("print enumerate")
enx = enumerate(xs)
print(list(enx))
for i in range(len(xs)):
    xs[i] = xs[i] * 2
print(xs)

enx2 = enumerate(xs)
print("enumerate after the loop")
print(list(enx2))

xx = [6, 7, 8, 9, 10]
for (index, val) in enumerate(xx):
    xx[index] = val ** 2
    print(index, val, xx[index])
print("we don't enumerate\n\n")

print("Problem 11.1\n")
print(list(range(10, -2, -2)))

print("Problem 11.3\n")
a = [1, 2, 3]
b = a[:]
b[0] = 5
print(b)
print(a)

print("problem 11.4")
this = ["I", "am", "not", "a", "crook"]
that = ["I", "am", "not", "a", "crook"]
print("Test 1: {0}".format(this is that))
that = this  # now they are both pointing to the same object
print("Test 2: {0}".format(this is that))

print("problem 10.2")
myList = []
myList.append(76)
myList.append(92.3)
myList.append("hello")
myList.append(True)
myList.append(4)
myList.append(76)
myList.append("Apple")
myList.insert(3, "cat")
myList.insert(0, 99)
myList.index("hello")
myList.count(76)
myList.remove(76)
myList.pop(True)
print(myList)

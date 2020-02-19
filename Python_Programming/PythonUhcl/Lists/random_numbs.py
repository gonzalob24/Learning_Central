import random

print("Problem 10.4")

myList = []
for i in range(100):
    xrand = random.randint(0, 1000)
    myList.append(xrand)
print(myList)
print(len(myList))


def max_num(lst):
    print(max(lst))
    maxim = 0
    for num in lst:
        if num > maxim:
            maxim = num
    return maxim


max_val = max_num(myList)
print(max_val)

ss = "Go Spot Go"
for achar in ss.split():
    print(achar)
print("b".upper())

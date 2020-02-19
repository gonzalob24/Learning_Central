import random

#Problem 2
myList = [76, 92.3, "hello", True, 4, 76]

print(myList)

myList2 = []
myList2.append(76)
myList2.append(92.3)
myList2.append("hello")
myList2.append(True)
myList2.append(4)
myList2.append(76)

print(myList2)

#problem3
myList.insert(2, "cat")
myList.insert(0, 99)
count76 = myList.count(76)
print(count76)
print(myList)
myList.remove(76)
myList.pop(4)
print(myList)


#problem 4
randIntegers = []
for n in range(100):
    randnum = random.randint(0, 1000)
    randIntegers.append(randnum)


def average(numList):
    avg = 0
    sum = 0
    for num in numList:
        sum += num
        avg = sum / 100;
    return avg


print(average(randIntegers))

#problem5
def maxNum(numList):
    max = 0
    for num in numList:
        if num > max:
            max = num
    return max

print(maxNum(randIntegers))

myList3 = [2, 3, 4]

#problem 6
def sum_of_squares(numList):
    sum = 0
    for num in numList:
        sum += num**2
    return sum

print(sum_of_squares(myList3))

#problem 7
def countOdd(numList):
    count = 0
    for num in numList:
        if num % 2 != 0:
            count += 1
    return count

print(countOdd(myList3))

#problem 10
stringList = ["Hello", "happy", "gonzalo", "Notfivewords"]

def countWordsLengthFive(strList):
    count = 0
    for word in strList:
        if len(word) == 5:
            count += 1
    return count

print(countWordsLengthFive(stringList))


#problem 11
def sumAllExceptFirstEven(numList):
    sum = 0
    index = 0
    while index < len(numList) and numList[index] % 2 != 0:
        sum += numList[index]
        index += 1
    return sum


myList4 = [3, 3, 3, 1, 5, 2, 3, 4]

print(sumAllExceptFirstEven(myList4))


#problem 12
myList5 = ["hello", "petter", "Gonzalo", "sam", "Alison"]

def count(strList):
    count = 0
    index = 0
    while index < len(strList) and strList[index] != "sam":
        count += 1
        index += 1
    return count

print(count(myList5))


#problem 14


def replace(strWord, old, new):
    tempStr = list(strWord)
    for char in tempStr:
        if char == old:
            tempStr[char] = new
    print(tempStr)

replace("Mississippi", "i", "I")


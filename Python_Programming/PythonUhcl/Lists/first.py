# iterative sum

def listsum(numList):
    theSum = 0
    for i in numList:
        theSum += i
    return theSum

print(listsum([1,3,5,7,9]))


# now with recursion

def listsum2(numList):
    if len(numList == 0):
        return numList[0]
    else:
        return numList[0] + numList[1:]


# convert to binary

def toStr(n, base):
    convertString = '0123456789ABCDEF'
    if n < base:
        return convertString[n]
    else:
        return toStr(n//base, base) + convertString[n%base]

print(toStr(1453, 16))

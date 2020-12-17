def invert(array):
    if len(array) == 0:
        return []

    return invert(array[1:]) + [array[0]]


print(invert([1, 2, 3, 4]))


def replaceWithZero(array):
    if len(array) == 0:
        return []

    if array[0] < 0:
        return [0] + replaceWithZero(array[1:])

    return [array[0]] + replaceWithZero(array[1:])


# print(replaceWithZero([1, 2, -3, -4, -5, -9]))


def replaceWithZero2(array, index):
    if index < len(array):
        if array[index] < 0:
            array[index] = 0
        replaceWithZero2(array, index + 1)
    # return [array[index]] + replaceWithZero2(array, index + 1)

    # return array
    return


test = [1, 2, -3, -4, -5, -9]
replaceWithZero2(test, 0)
print(test)

def sortArray(array, length):
    # if length == 0:
    #     return [array[length]]

    # lastNum = array[length - 1]
    # nextNum = 0
    # for num in range(length):
    #     if lastNum < nextNum:
    #         nextNum = lastNum
    #         array[length - 1] = nextNum
    # return sortArray(array[:], length - 1)
    if length <= 1:
        return

    sortArray(array, length - 1)

    # get lastElement
    lastElement = array[length - 1]
    temp = length - 2
    while temp >= 0 and array[temp] > lastElement:
        array[temp + 1] = array[temp]
        temp -= 1

    array[temp + 1] = lastElement


test = [5, 4, 2, 3, 1]
print(test)
print(sortArray(test, 5))
print(test)

def minValue(array):
    # array.sort()
    # return array[0]

    # return sorted(array)[0]
    minValue = float('inf')
    for item in array:
        if item < minValue:
            minValue = item
    return minValue


print(minValue([9, 2, 3, 6]))

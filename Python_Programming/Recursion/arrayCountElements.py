def countEl(array, num):
    if array == []:
        return 0

    if array[0] == num:
        return 1 + countEl(array[1:], num)
    return countEl(array[1:], num)


print(countEl([1, 2, 3, 1], 1))

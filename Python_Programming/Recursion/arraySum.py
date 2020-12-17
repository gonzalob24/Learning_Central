def sumArray(array, index):
    if index == len(array) - 1:
        return array[index]

    if index == 0:
        return (array[index] + sumArray(array, index + 1)) / len(array)

    return array[index] + sumArray(array, index + 1)


print(sumArray([10, 2, 3, 4, 8, 0], 0))

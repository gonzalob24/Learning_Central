def indexOf(arr, element, index):
    if index == len(arr):
        return - 1
    if arr[index] == element:
        return index

    return indexOf(arr, element, index + 1)


print(indexOf([9, 8, 2, 8, 3, 7], 1, 0))

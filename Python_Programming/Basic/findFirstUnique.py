def findFirstUnique(array):
    unique = False
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] != array[j]:
                unique = True
            else:
                unique = False
        if unique:
            return array[i]
    return array[0]


print(findFirstUnique([4, 5, 1, 2, 0, 4]))

def merSortedArrays(array1, array2):
    # Store merged array in results
    results = []
    idx1 = 0
    idx2 = 0
    # pick array with smallest length
    for idx in range(len(array1) + len(array2)):
        if not array1 and not array2:
            break
        if idx2 == len(array2):
            if idx1 < len(array1):
                results += array1[idx1:]
            break
        if idx1 == len(array1):
            if idx2 < len(array2):
                results += array2[idx2:]
            break
        if array1[idx1] <= array2[idx2]:
            results.append(array1[idx1])
            idx1 += 1
        elif array2[idx2] <= array1[idx1]:
            results.append(array2[idx2])
            idx2 += 1

    return results


print(merSortedArrays([1, 3, 4, 5], [2, 6, 7, 8]))
print(merSortedArrays([-133, -100, 0, 4], [-2000, 2000]))
print(merSortedArrays([4, 4, 4, 4, 100], [-1, 2, 3, 44, 2000]))
print(merSortedArrays([4, 5, 6], [-2, -1, 0, 7]))

test = [1, 2, 3]
print(test)
test.insert(1, 4)
print(test)

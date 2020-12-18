def merge(ar1, ar2):
    if ar1 == []:
        return ar2

    if ar2 == []:
        return ar1

    if ar1[0] <= ar2[0]:
        return [ar1[0]] + merge(ar1[1:], ar2)

    if ar2[0] <= ar1[0]:
        return [ar2[0]] + merge(ar1, ar2[1:])


print(merge([1, 3, 4, 5], [2, 6, 7, 8]))
print(merge([-133, -100, 0, 4], [-2000, 2000]))
print(merge([4, 4, 4, 4, 100], [-1, 2, 3, 44, 2000]))
print(merge([4, 5, 6], [-2, -1, 0, 7]))

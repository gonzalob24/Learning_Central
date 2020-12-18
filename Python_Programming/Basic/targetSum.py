def targetSum(array, target):
    """
    Time --> O(n^2)
    space --> O(1)
    """
    for i in range(len(array)):  # -- n
        for j in range(i + 1, len(array)):  # n
            if array[i] + array[j] == target:  # n^2
                return [array[i], array[j]]
    return []


print(targetSum([1, 21, 3, 14, 5, 60, 7, 6], 81))
print(targetSum([1, 2, 3, 4], 5))

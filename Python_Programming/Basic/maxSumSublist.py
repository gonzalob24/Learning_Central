def maxSum(array):
    """
    brute force solution
    """
    if len(array) < 1:
        return 0

    sumOfSublist = 0
    maxSum = 0
    # for i in range(len(array)):
    #     for j in range(i + 1, len(array)):
    #         sumOfSublist += array[j]
    #         if sumOfSublist > maxSum:
    #             maxSum = sumOfSublist
    #     sumOfSublist = 0

    for i in range(len(array)):
        if sumOfSublist < 0:
            sumOfSublist = array[i]
        else:
            sumOfSublist += array[i]

        if maxSum < sumOfSublist:
            maxSum = sumOfSublist

    return maxSum


print(maxSum([-4, 2, -5, 1, 2, 3, 6, -5, 1]))


def f(i, values=[]):
    values.append(i)
    print(values)
    return values


f(1)
f(2)
f(3)

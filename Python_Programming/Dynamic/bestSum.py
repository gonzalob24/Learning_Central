def bestSum(targetSum, nums):
    if targetSum < 0:
        return None

    if targetSum == 0:
        return []

    shortestCombination = None  # this
    for num in nums:
        remainder = targetSum - num
        remainderResult = bestSum(remainder, nums)
        if remainderResult != None:
            combination = [*remainderResult, num]
            if shortestCombination == None or len(combination) < len(shortestCombination):
                shortestCombination = combination

    # if I do not enter the for loop up top then there are no combos and return None
    return shortestCombination


print(bestSum(7, [5, 3, 4, 7]))  # [7]
print(bestSum(8, [2, 3, 5]))  # [3,5]
print(bestSum(8, [1, 4, 5]))  # [4,4]
print(bestSum(100, [1, 2, 5, 25]))  # [25,25,25,25]

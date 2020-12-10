# Combinatoric Problem
def howSum(targetSum, nums, memo={}):
    if targetSum in memo:
        return memo[targetSum]

    if targetSum == 0:
        return []

    if targetSum < 0:
        return None

    for num in nums:
        remainder = targetSum - num
        # howSum may return [] or None
        remainderResult = howSum(remainder, nums, memo)
        if remainderResult != None:
            memo[targetSum] = [*remainderResult, num]
            return memo[targetSum]

    memo[targetSum] = None
    return None


# arr = [1, [2, 3], 4, 5]
# print(*arr)


print(howSum(7, [2, 3], {}))
print(howSum(7, [5, 3, 4, 7], {}))
print(howSum(7, [2, 4], {}))
print(howSum(8, [2, 3, 5], {}))
print(howSum(300, [7, 14], {}))

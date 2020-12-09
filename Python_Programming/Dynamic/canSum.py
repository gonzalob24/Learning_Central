def canSum(targetSum, nums, memo={}):
    # which argument directly impacts the return value. nums does not change, targetSum changes.
    if targetSum in memo:
        return memo[targetSum]
    # base case when to stop looking for sum
    if targetSum == 0:
        return True

    if targetSum < 0:
        return False

    for num in nums:
        remainder = targetSum - num
        if canSum(remainder, nums, memo) == True:
            memo[targetSum] = True
            return True
    memo[targetSum] = False
    return False


def canSum1(targetSum, nums):
    # which argument directly impacts the return value. nums does not change, targetSum changes.

    # base case when to stop looking for sum
    if targetSum == 0:
        return True

    if targetSum < 0:
        return False

    for num in nums:
        remainder = targetSum - num
        if canSum1(remainder, nums) == True:
            return True
    return False


print(canSum(7, [2, 3], {}))
print(canSum(7, [5, 3, 4, 7], {}))
print(canSum(7, [2, 4], {}))
print(canSum(8, [2, 3, 5], {}))
print(canSum(300, [7, 14], {}))

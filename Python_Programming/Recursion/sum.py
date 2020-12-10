def sumNums(nums):
    # O(n^2) due to the slice
    # base case, ends recursion calls
    if len(nums) == 0:
        return 0

    # recursive case
    return nums[0] + sumNums(nums[1:])


# print(sumNums([1, 5, 7, -2]))

def sumNums2(nums):
    # O(n) -- Time/Space
    return _sumNums(nums, 0)


def _sumNums(array, index):
    # base case, ends recursion calls
    if index == len(array):
        return 0

    # recursive case
    return array[index] + _sumNums(array, index + 1)


print(sumNums2([1, 5, 7, -2]))

import math
import collections

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


# print(howSum(7, [2, 3], {}))
# print(howSum(7, [5, 3, 4, 7], {}))
# print(howSum(7, [2, 4], {}))
# print(howSum(8, [2, 3, 5], {}))
# print(howSum(300, [7, 14], {}))
arr = [1, 2, 3]

arr[:] = []
n = []
a = [1, 2, 3]
# n[:] = a[:]
# n[0] = 'H'
p = [8, 4, 6, 2, 3]


def finalPrices(prices):
    stk = []
    for i, p in enumerate(prices):
        while stk and prices[stk[-1]] >= p:
            prices[stk.pop()] -= p
        stk.append(i)
    return prices


# print(finalPrices([8, 4, 6, 2, 3]))
# print('True or false')
# print(n and (p[n[-1]] >= 8))
# print(p[n.pop()])
moves = 'UUUDDDLLL'
c = collections.Counter(moves)
print(c.items())
# for k, v in c.items():
#     print(k, v)
print(round(4.42))
print(min(1, 2))

ar = [[1], [2, 3]]
print(ar.index([1]))
name = "Gonzalo"
print(name.find("w"))
ar2 = [[1], [2, 3, 4]]
ar3 = [1, 2, 3, 4]
for n in ar2:
    print(ar3[1:len(n)] == n)
art = [1, 2, 3, 4]
art2 = [6, 2, 6, 5, 1, 2]
art2.sort()
print(art[::2])
print(art2[::2])
print((art2[::2]))

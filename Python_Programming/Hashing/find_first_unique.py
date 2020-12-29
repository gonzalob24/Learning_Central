def findFirstUnique(lst):
    memo = {}
    for item in lst:
        if item not in memo:
            memo[item] = 1
        else:
            memo[item] += 1

    for item in lst:
        if memo[item] == 1:
            return item


print(findFirstUnique([9, 2, 3, 2, 6, 6]))
print(findFirstUnique([4, 5, 1, 2, 0, 4]))

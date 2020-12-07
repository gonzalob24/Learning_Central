"""
Given N count the nunber of ways to express N as snum of 1, 3, 4

Example: 
    input: 4
    Output: {1,3},{3,1}, {1,1,1,1}
"""


def waysToCountN(n):
    if n == 0 or n == 1 or n == 2:
        return 1

    if n == 3:
        return 2

    subtract1 = waysToCountN(n - 1)
    subtract3 = waysToCountN(n - 3)
    subtract4 = waysToCountN(n - 4)

    return subtract1 + subtract3 + subtract4


print(waysToCountN(5))

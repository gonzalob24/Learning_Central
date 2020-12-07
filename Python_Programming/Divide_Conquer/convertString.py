# Hard
def findMinOperations(s1, s2, idx1, idx2):
    # base case if I reach end of s1, delete remaining characters of s2
    if idx1 == len(s1):
        return len(s2) - idx2

    # base case: if i reach end of s2 insert remaining characters of s2 into s2
    if idx2 == len(s2):
        return len(s1) - idx1

    if s1[idx1] == s2[idx2]:
        return findMinOperations(s1, s2, idx1 + 1, idx2 + 1)

    c1 = 1 + findMinOperations(s1, s2, idx1 + 1, idx2)  # insert
    c2 = 1 + findMinOperations(s1, s2, idx1, idx2 + 1)  # delete
    c3 = 1 + findMinOperations(s1, s2, idx1 + 1, idx2 + 1)  # replacement

    return min(c1, c2, c3)


print(findMinOperations("table", "tcble", 0, 0))

def waysToGetN(n):
    # initialize an empty array to store resuable sub problems
    dp = [0] * (n + 1)

    # helper function to do top down aproach
    def waysToGetN_TopDown(dp, n):
        if n == 0 or n == 1 or n == 2:
            return 1
        if n == 3:
            return 2
        if dp[n] == 0:  # means we have not solved this sub problem and should store solution
            subtract1 = waysToGetN_TopDown(dp, n - 1)
            subtract2 = waysToGetN_TopDown(dp, n - 3)
            subtract3 = waysToGetN_TopDown(dp, n - 4)
            # store the sum in the dp array
            dp[n] = subtract1 + subtract2 + subtract3

        return dp[n]
    return waysToGetN_TopDown(dp, n)


n = 2
arr = [0] * (n + 1)
print(len(arr))

# Leet code
def numDecodings(s):
    count = 0

    for n in range(len(s)):
        if int(s[n]) > 0 or int(s[n]) <= 9:
            count += 1

    for n in range(len(s) - 1):
        if int(s[n:n+2]) <= 26:
            count += 1
    return count


def jumpGame(arr):
    """
    Backtracking and dynamic programming

    """
    lastGoodIndexPosition = len(arr) - 1

    for n in reversed(range(len(arr))):
        print(n)
        if(n + arr[n] >= lastGoodIndexPosition):
            lastGoodIndexPosition = n
    return lastGoodIndexPosition == 0


def jumpGame_myReversion(arr):
    max_reach = 0
    for current_index in range(len(arr)):
        if current_index > max_reach:
            return False
        # update max reach after every step
        max_reach = max(max_reach, current_index + arr[current_index])
    return True


print(jumpGame_myReversion([2, 3, 1, 1, 4]))

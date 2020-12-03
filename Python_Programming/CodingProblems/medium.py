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

print(numDecodings("12"))

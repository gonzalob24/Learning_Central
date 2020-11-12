import time

"""
Reverse a digit brute force
"""

def reverseInt(n):
    start = time.time()
    if n < 10 and n >=0:
        reverse = str(n)
    else:
        if n > 0:
            n = str(n)
            reverse = n[::-1]
        else:
            n = str(n)
            reverse = n[0] + n[:0:-1]
    end = time.time()
    total = end - start
    return reverse, total

def using_mod_reverseInt(n):
    start = time.time()
    tempN = abs(n)
    reverse = 0
    while tempN > 0:
        lastInt = tempN% 10
        reverse = reverse * 10 + lastInt
        tempN = tempN // 10

    end = time.time()
    total = end - start
    return -reverse if n < 0 else reverse , total

num, t = reverseInt(-75)
print(num, t)
num2, t2 = using_mod_reverseInt(-75)
print(num2, t2)
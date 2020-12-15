def factorial(n):
    """
    4! = 4*3*2*1
    1! = 1
    0! = 1
    """

    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


print(factorial(4))
print(factorial(5))

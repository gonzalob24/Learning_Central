def fib(n):
    # O(2^n) -- Time
    # O(n) -- Time
    # base, we know that the first two numbers are 1, 1
    if n < 0:
        return "Number has to be positive!"
    if n < 2:
        return n
    return fib(n - 2) + fib(n - 1)
    # recursive case


print(fib(6))
print(fib(7))
print(fib(-1))

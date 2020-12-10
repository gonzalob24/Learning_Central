def fib(n):
    # O(2^n) -- Time
    # O(n) -- Time
    # base, we know that the first two numbers are 1, 1
    if n < 0:
        return "n can't be negative"
    if n == 1 or n == 2:
        return 1

    return fib(n - 1) + fib(n - 2)
    # recursive case


print(fib(6))
print(fib(7))
print(fib(-1))

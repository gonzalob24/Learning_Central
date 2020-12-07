# O(2^n)
def fib(nth):
    # first two numbers are 0 and 1 as given
    if nth < 0:
        return "Number can't be less than 1"
    elif nth < 2:
        return nth
    else:
        return fib(nth - 1) + fib(nth - 2)


print(fib(6))
print(fib(7))
print(fib(8))

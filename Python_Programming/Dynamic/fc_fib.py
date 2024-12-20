# memoization
#  store duplicate subproblems: use an array or object: key --> f(n) value: return of f(n)
def fib(n, memo={}):

    if n in memo:
        return memo[n]
    if n < 2:
        return n
    # save value in memo object
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]


print(fib(6))
print(fib(7))
print(fib(8))
print(fib(50))

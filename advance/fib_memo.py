memo = dict()


def fib(n):
    f = 0
    if n in memo:
        return memo[n]

    if n <= 0:
        return 0
    if n <= 2:
        return 1
    f = fib(n - 1) + fib(n - 2)
    memo[n] = f
    return f


for n in range(1,101):
    print(fib(n))

print(memo)

memo = dict()


def fib(n):

    n = abs(n)

    if n in memo:
        return memo[n]

    if n <= 2:
        f = 1
    else:
        f = fib(n - 1) + fib(n - 2)

    memo[n] = f

    return f


for i in range(1, 10001):
    print(fib(i))

# print(memo)

fib_memo = {}


def fib_for(num):
    for k in range(1, num + 1):
        if k <= 2:
            f = 1
        else:
            f = fib_memo[k - 1] + fib_memo[k - 2]

    fib_memo[num] = f
    return f


# for i in range(1, 101):
#     print(fib_for(i))

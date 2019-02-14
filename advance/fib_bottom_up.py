def fib(n):

    if n <= 2:
        return 1

    a, b = 1, 1

    for i in range(n-2):
        a, b = a + b, a

    return a


for x in range(1, 100):
    print(fib(x))



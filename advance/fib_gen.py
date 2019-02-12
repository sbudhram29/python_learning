def fib(n):
    """
    A Generate to provide Fib to the nth
    :param n:
    :return: int
    """

    a, b = 0, 1

    for _ in range(n):
        a, b = a + b, a
        yield a


for x in fib(100):
    print(x)

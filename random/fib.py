def fib(n):
    """
    A Generate to provide Fib to the nth
    :param n:
    :return: int
    """

    if n < 1:
        yield 0

    a, b = 0, 1

    for _ in range(n):
        a, b = a + b, a
        yield a

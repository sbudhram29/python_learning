import math


def fib(n):
    phi = ( 1 + math.sqrt(5)) / 2

    return int(phi**n / math.sqrt(5))


for x in range(1000):
    print(fib(x))


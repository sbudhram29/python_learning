"""
Fib
"""
from functools import lru_cache


@lru_cache()
def fib(n):
    """
    >>> fib(38)
    39088169
    """
    if n <= 0:
        return 0
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)


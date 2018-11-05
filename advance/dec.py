def logme(func):
    import logging
    logging.basicConfig(level=logging.DEBUG)

    def inner(*args, **kwargs):
        logging.debug(f"Called {func.__name__, args, kwargs}")
        return func(*args, **kwargs)
    inner.__name__ = func.__name__
    inner.__doc__ = func.__doc__
    return inner


@logme
def print_this(a, b, switch=True):
    return a - b if not switch else b - a


print_this(1, 2)
print_this(1, 2, switch=False)

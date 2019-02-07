from functools import reduce
import timeit


def list_mul(list_of_numbers):
    result = []
    for i, n in enumerate(list_of_numbers):
        current = [x for x in list_of_numbers]
        current.pop(i)
        result.append(reduce(lambda x, y: x * y, current, 1))

    return result


def list_mul2(list_of_numbers):
    result = []
    for i, n in enumerate(list_of_numbers):
        result.append(int(reduce(lambda x, y: x * y, list_of_numbers, 1) / n))

    return result


if __name__ == '__main__':
    import timeit

    print(list_mul([1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5]))

    print(timeit.timeit("list_mul([1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5])",
                        setup="from __main__ import list_mul", number=100))

    print(timeit.timeit("list_mul2([1, 2, 3, 4, 5])",
                        setup="from __main__ import list_mul2", number=100))

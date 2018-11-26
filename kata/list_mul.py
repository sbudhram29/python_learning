from functools import reduce


def list_mul(list_of_numbers):
    result = []
    for i, n in enumerate(list_of_numbers):
        current = [x for x in list_of_numbers]
        current.pop(i)
        result.append(reduce(lambda x, y: x * y, current, 1))

    return result


print(list_mul([1, 2, 3, 4, 5]))
print(list_mul([1, 2, 3]))
print(list_mul([3, 2, 1]))

my_tuple = 5,

print(my_tuple)

a = 20
b = 5

a, b = b, a

print(b)
print(a)


def multiply(*args):
    args_list = list(args)
    print(args_list)
    result = args_list[:1][0]

    for arg in args_list:
        result *= arg

    return result


print(multiply(1, 2, 3))

# [(1, 'a'), (2, 'b'), (3, 'c')]


def combo(*args):
    result = []
    for index, value in enumerate(args[0]):
        result.append((value, args[1][index]))
    return result


print(combo([1, 2, 3], 'abc'))

def swap(x, y):
    x = x ^ y
    y = x ^ y
    x = x ^ y

    return x, y


print(swap(1,2))

print(swap(3,2))

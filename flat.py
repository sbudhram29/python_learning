def flatten(arr):
    if len(arr) == 0:
        return arr
    if isinstance(arr[0], list):
        return flatten(arr[0]) + flatten(arr[1:])
    return [arr[0]] + flatten(arr[1:])


print(flatten([1, 2, 3, [1, 2, [3, 5]]]))
print(flatten([1, 2, 3, [1, [4, 5, 6], 2, [3, 5]]]))

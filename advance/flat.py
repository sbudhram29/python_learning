def flatten(arr):
    if len(arr) == 0:
        return arr
    if type(arr[0]) is list:
        return flatten(arr[0]) + flatten(arr[1:])
    return [arr[0]] + flatten(arr[1:])


print(flatten([1, 2, 3, [1, 2, [3, 5]]]))
print(flatten([1, 2, 3, [1, [4, 5, 6], 2, [3, 5]]]))
print(flatten([1, 2, 3, [1, [4, 5, 6], 2, [3, 5]]]))
print(flatten([1, 2, 3, [1, [4, 5, 6], 2, [3, 5]]]))
print(flatten([1, 2, 3, [1, [4, 5, 6], 2, [3, 5]]]))
print(flatten([]))
print(flatten([[1, 3, 4, 5, 6, [[[[[1, 2, 3, 4, [5, 6, 7]]]]]]]]))

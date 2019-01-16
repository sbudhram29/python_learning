def snail(array):
    res = []
    return addToResult(array, res)


def addToResult(arr, res):

    innerArray = []

    if len(arr[1:-1]):
        for i in arr[1:-1]:
            innerArray.append(i[1:-1])

    for i in arr[0]:
        res.append(i)

    for i in arr[1:]:
        res.append(i[-1])

    for i in arr[-1][:-1][::-1]:
        res.append(i)

    for i in arr[1:-1][::-1]:
        res.append(i[0])

    if len(innerArray):
        addToResult(innerArray, res)

    return res


array = [[1, 2, 3, 4, 5],
         [6, 7, 8, 9, 10],
         [11, 12, 13, 14, 15],
         [16, 17, 18, 19, 20],
         [21, 22, 23, 24, 25]]

print(snail(array))
# print(snail([[]]))


def snail(array):
    if array:
        # force to list because zip returns a list of tuples
        top_row = list(array[0])
        # rotate the array by switching remaining rows & columns with zip
        # the * expands the remaining rows so they can be matched by column
        rotated_array = list(zip(*array[1:]))
        # then reverse rows to make the formerly last column the next top row
        rotated_array = rotated_array[::-1]
        return top_row + snail(rotated_array)
    else:
        return []


def snail2(array):
    print(list(zip(*array[1:]))[::-1])
    return
    return list(array[0]) + snail2(list(zip(*array[1:]))[::-1]) if array else []


print(snail2(array))

def xor_queries(arr, queries):
    for i in range(len(arr) - 1):
        print(i, i + 1, arr[i + 1], arr[i], arr)
        arr[i + 1] ^= arr[i]


    print(arr)
    return [arr[j] ^ arr[i - 1] if i else arr[j] for i, j in queries]



print(xor_queries([1,3,4,8], [[0,1],[1,2],[0,3],[3,3]]))
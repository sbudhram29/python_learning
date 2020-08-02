from collections import Counter

def permute(S):
    # get the count of each character in a dict
    C = Counter(S)
    # get unique chars
    U = list(C.keys())
    # get and array of count
    A = list(C.values())

    # create a fill array to store result
    res = list(S)

    # create a array to store permute string
    ans = []

    # utils function to generate permute string
    return permute_util(U, A, res, ans)


def permute_util(U, A, res, ans, level = 0):

    if len(res) == level:
        ans.append(''.join(res))

    for i in range(len(U)):
        if A[i] == 0:
            continue

        res[level] = U[i]

        A[i] -= 1
        permute_util(U, A, res, ans, level + 1)
        A[i] += 1

    return ans






print(permute('AACD'))
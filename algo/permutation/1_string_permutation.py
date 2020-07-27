from collections import Counter


def permute(S):
    C = Counter(S)
    unique_chars = list(C.keys())
    chars_count = list(C.values())

    result = [False for _ in S]
    return permute_util(unique_chars, chars_count, result, 0)




def permute_util(U, C, result, level):
    if level == len(result):
        print(''.join(result))
        return

    for i in range(len(U)):
        if C[i] == 0:
            continue

        result[level] = U[i]
        C[i] -= 1
        permute_util(U, C, result, level + 1)
        C[i] += 1



permute('AACSS')
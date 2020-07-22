arr = [1,2,3,4,5,5,6,6,7,7,8]

def remove_dup(A):
    if not A:
        return 0

    valid = 1
    for j in range(1, len(A)):

        if A[j] != A[valid - 1]:
            A[valid] = A[j]
            valid += 1
    return valid




print(remove_dup(arr))
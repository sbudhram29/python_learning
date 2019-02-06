def sum_of_k(list_of_numbers, k):
    '''
    determine if two int in list can be
    added to sum up to k
    '''

    seen = []
    for n in list_of_numbers:
        needed = k - n
        if (needed in seen or needed == 0):
            return True
        seen.append(n)

    return False

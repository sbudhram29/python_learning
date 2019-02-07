def sum_of_k(list_of_numbers: list, k: int) -> bool:
    '''
    determine if two int in list can be
    added to sum up to k
    '''
    seen: list = []

    for num in list_of_numbers:
        needed = k - num
        if (needed in seen or needed == 0):
            return True
        seen.append(num)

    return False

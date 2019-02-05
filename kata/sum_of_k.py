def sum_of_k(list_of_numbers, k):

    seen = []
    for n in list_of_numbers:
        needed = k - n
        if needed in seen:
            return True
        else:
            seen.append(n)

    return False


# nums = [10, 15, 3, 7]
# k = 17

# print(sum_of_k(nums, k))

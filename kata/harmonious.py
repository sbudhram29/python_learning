from collections import Counter

def find_lhs(nums):

    if len(nums) < 2:
        return 0

    c = Counter(nums)
    res = []

    for k in list(c):
        if k + 1 in c:
           res.append(c[k] + c[k +1])

    return max(res)






print(find_lhs([1,3,2,2,5,2,3,7]))
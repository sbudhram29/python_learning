from collections import Counter

def sliding_window(B, S):
    if not B or not S:
        return

    c_hash = Counter(S)
    count_needed = len(c_hash)
    count_valid = 0
    left, right = 0, 0

    res = float('inf'), 0, 0

    curr_hash = {}

    while right < len(B):
        c = B[right]
        curr_hash[c] = curr_hash.get(c,0) + 1

        if c in c_hash and curr_hash[c] == c_hash[c]:
            count_valid += 1

        while left <= right and count_valid == count_needed:
            c = B[left]

            if res[0] > right - left + 1:
                res = right - left + 1, left, right

            curr_hash[c] -= 1

            if c in c_hash and curr_hash[c] < c_hash[c]:
                count_valid -= 1

            left += 1

        right += 1

    return res

B = "xyyszyzyxc"
S = "xyz"

print(sliding_window(B, S))


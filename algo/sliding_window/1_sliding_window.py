from collections import Counter
def sliding_window(s, t):
    if not s or not t:
        return ""

    char_hash = Counter(t)
    required = len(char_hash)

    left, right = 0, 0

    valid = 0

    curr_window = {}
    ans = float('inf'), None, None

    while right < len(s):

        c = s[right]

        curr_window[c] = curr_window.get(c, 0) + 1

        if c in char_hash and curr_window[c]  == char_hash[c]:
            valid += 1

        while left <= right and valid == required:
            c = s[left]

            range_length = right - left + 1
            if range_length < ans[0]:
                ans = range_length, left, right

            curr_window[c] -= 1

            if c in char_hash and curr_window[c] < char_hash[c]:
                valid -= 1

            left += 1


        right += 1


    if ans[0] == float('inf'):
        return ""

    return s[ans[1]:ans[2] + 1]





S = "xyyzyzyx"
T = "xyz"

print(sliding_window(S, T))



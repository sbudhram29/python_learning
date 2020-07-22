from collections import Counter
def min_window(s, t):
    if not t or not s:
        return ""

    dict_t = Counter(t)

    required = len(dict_t)

    left, right = 0, 0

    valid = 0

    counts = {}

    ans = float("inf"), None, None

    while right < len(s):
        c = s[right]
        counts[c] = counts.get(c, 0) + 1

        if c in dict_t and counts[c] == dict_t[c]:
            valid += 1

        while left <= right and valid == required:
            c = s[left]

            if right - left + 1 < ans[0]:
                ans = (right-left + 1), left, right
            #
            counts[c] -= 1
            if c in dict_t and counts[c] < dict_t[c]:
                valid -= 1

            left += 1

        right += 1


    print(ans)
    return "" if ans[0] == float("inf") else s[ans[1]: ans[2] + 1]


S = "xyyzyzyx"
T = "xyz"

print(min_window(S, T))
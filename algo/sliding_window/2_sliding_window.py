from collections import Counter
B = "xyyszyzyxc"
S = "xyz"


def s_window(B, S):
    if not B or not S:
        return ""

    # get hash of small (S) string
    chars_count = Counter(S)

    # get length of hash
    required_valid = len(chars_count)
    # create variable to keep valid count
    current_valid = 0

    # create index for left, right
    left, right = 0, 0

    # create hash for window
    win = {}

    # create a tuple for result

    result = float('inf'), None, None

    # traverse big string (B) and check window

    while right < len(B):
        # get current char
        c = B[right]
        # update current char count in win hash
        win[c] = win.get(c, 0) + 1

        #check to see if valid
        if c in chars_count and win[c] == chars_count[c]:
            current_valid += 1

        #while valid decrease window and check if still valid
        while left < right and required_valid == current_valid:
            # get char at left
            c = B[left]

            # check to see if window is smallest
            if right - left + 1 < result[0]:
                # update if window is smallest
                result = right - left + 1, left , right

            # remove current char from win hash
            win[c] -= 1

            # check to see if not valid
            if c in chars_count and win[c] < chars_count[c]:
                current_valid -= 1

            left += 1

        right += 1


    return result


print(s_window(B, S))


def find_longest(s1, s2):

    matches = []
    s2Arr = list(s2)

    for letter in s1:
        for k, v in enumerate(s2Arr):
            if letter == v:
                matches.append(letter)
                if k == 0:
                    del s2Arr[k]
                else:
                    s2Arr = s2Arr[k:]
                break
    return ''.join(matches)


# print(find_longest('ABAXDC', 'BACBAD'))
# print(find_longest('AGGTAB', 'GCTXAYB'))
# print(find_longest('aaaa', 'aa'))

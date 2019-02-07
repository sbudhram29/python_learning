
def find_longest(s1, s2, matches = []):
    current_matches = []
    s2Arr = list(s2)

    for letter in s1:
        for k, v in enumerate(s2Arr):
            if letter == v:
                current_matches.append(letter)
                if k == 0:
                    del s2Arr[k]
                else:
                    s2Arr = s2Arr[k+1:]
                break

    if len(current_matches) > len(matches):
        matches = [*current_matches]

    if len(matches) < len(s1):
        return find_longest(s1[1:], s2, matches)
    else:
        return ''.join(matches)





# print(find_longest('ABAXDC', 'BACBAD'))
# print(find_longest('AGGTAB', 'GCTXAYB'))
# print(find_longest('aaaa', 'aa'))

from collections import Counter

def permute(S):
    if not len(S):
        return ""

    # get the count of each character in a dict
    C = Counter(S)
    # get unique chars
    letters = list(C.keys())
    # get and array of count
    letter_count = list(C.values())

    # create a fill array to store result
    result = list(S)

    # create a array to store permute string
    ans = []

    # utils function to generate permute string
    utils(letters, letter_count, result, 0, ans)

    return ans




def utils(letters, letter_count, result, level, ans):

    if level == len(result):
        ans.append(''.join(result))

    for i in range(len(letters)):
        if letter_count[i] < 1:
            continue

        result[level] = letters[i]
        letter_count[i] -= 1
        utils(letters,letter_count, result, level + 1, ans)
        letter_count[i] += 1




print(permute('AACD'))
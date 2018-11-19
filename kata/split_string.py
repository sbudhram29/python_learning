def solution(s):
    result = []
    sub_string = ''
    for i in range(0, len(s), 2):

        sub_string = s[i:i+2]
        if len(sub_string) == 1:
            sub_string += '_'

        result.append(sub_string)

    return result


def solution2(s):
    return [(s + "_")[i:i + 2] for i in range(0, len(s), 2)]


print(solution('abc'))  # should return ['ab', 'c_']
print(solution('abcdef'))  # should return ['ab', 'cd', 'ef']

print(solution2('abc'))  # should return ['ab', 'c_']
print(solution2('abcdef'))  # should return ['ab', 'cd', 'ef']


t9 = {
    "2": ['a', 'b', 'c'],
    "3": ['d', 'e', 'f'],
    "4": ['g', 'h', 'i'],
    "5": ['j', 'k', 'l'],
    "6": ['m', 'n', 'o', 'p'],
    "7": ['q', 'r', 's'],
    "8": ['t', 'u', 'v', 'w'],
    "9": ['x', 'y', 'z'],
}

def gen_words(s, words= ['']):
    if len(s) == 0:
        return words

    for char in s:
        temp = []
        for letter in t9[char]:
            for word in words:
                temp.append(word + letter)

        words = temp

    return words


sean = gen_words('7326')
landon = gen_words('526366')

print('sean' in sean)
print('landon' in landon)


def valid_parentheses(string):
    openString = 0
    for letter in string:
        if letter == ')' and openString == 0:
            return False
        if letter == '(':
            openString += 1
        if letter == ')':
            openString -= 1

    if openString:
        return False
    else:
        return True


print(valid_parentheses(")test("))
print(valid_parentheses("hi())("))
print(valid_parentheses("  ("))
print(valid_parentheses(""))
print(valid_parentheses("hi(hi)()"))

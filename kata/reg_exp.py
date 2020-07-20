import re


def reg_exp(s):

    """
    '.' matches any character
    '^' start of string
    '$' end of string

    '*' 0 or more repetition
    '+' matches 1 0r more
    '?' 0 or 1
    {m} exactly m copies
    {m,n} matches m to n repetitions
    {m,n} ? matches m to n repetitions of preceding RE
    '[]' indicates a set of characters
    '|' matches a or b
    '/' escapes special character
    """

    match = r'[a-zA-Z0-9]+@[a-zA-Z0-9_]+\.[a-zA-Z0-9]+'
    return match


email_str = "sbudhram@gmail.com|scha@gnamil|ebudhram@gmail.com"

for email in re.findall(reg_exp(email_str), email_str):
    print(email)


numbers = '718-792-3260|718-822-4762|646-206-7603|111222555'

phone_match = r'[0-9]{3}\-[0-9]{3}\-[0-9]{4}'

for p_number in re.findall(phone_match, numbers):
    print(p_number)

for letter in "hello":
    print(letter)


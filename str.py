# s ='hello'
# a = ['22','gga','22','55125521']
#
# print(', '.join(x for x in a if len(x)>=3))

s = ')('


def valid_parentheses(paren_str):
    if len(paren_str) == 0:
        return True
    if '()' not in paren_str:
        return False

    s = paren_str.replace('()', '')
    return valid_parentheses(s)

print(valid_parentheses(s))
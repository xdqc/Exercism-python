import string


def cipher(c='', k=0):
    if c.islower():
        return chr((ord(c) + k - ord('a')) % 26 + ord('a'))
    elif c.isupper():
        return chr(ord(c) + k) if ord(c) + k <= ord('Z') else chr(ord(c) + k - 26)
    else:
        return c


def rotate(text='', key=0):
    trans_lowercase = string.ascii_lowercase[key:] + string.ascii_lowercase[:key]
    trans_uppercase = string.ascii_uppercase[key:] + string.ascii_uppercase[:key]
    table = str.maketrans(string.ascii_letters, trans_lowercase + trans_uppercase)
    return str.translate(text, table)




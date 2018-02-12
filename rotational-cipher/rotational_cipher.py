import re


def cipher(c='', k=0):
    if c.islower():
        return chr((ord(c) + k - ord('a')) % 26 + ord('a'))
    elif c.isupper():
        return chr(ord(c) + k) if ord(c) + k <= ord('Z') else chr(ord(c) + k - 26)
    else:
        return c


def rotate(text='', key=0):
    re.sub('\s+', ' ', text)
    text = map(lambda c: cipher(c, key), text)
    return ''.join(list(text))

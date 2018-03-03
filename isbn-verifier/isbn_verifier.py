import re


def dot(v1, v2):
    return sum(x * y for x, y in zip(v1, v2))


def verify(isbn=''):
    isbn = isbn.replace('-', '').upper()
    if not re.match('^\d{9}[\dX]$', isbn):
        return False
    isbn = [int(k) if k != 'X' else 10 for k in isbn]
    return dot(isbn, range(10, 0, -1)) % 11 == 0

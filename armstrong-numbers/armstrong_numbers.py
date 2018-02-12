from functools import reduce


def is_armstrong(number):
    num = list(map(int, str(number)))
    return reduce(lambda s, i: s + i ** len(num), num, 0) == number

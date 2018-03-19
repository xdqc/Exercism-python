import math


def square_of_sum(count):
    return math.pow(sum(range(1, count+1)), 2)


def sum_of_squares(count):
    return sum(list(map(lambda x: x*x, range(1, count+1))))


def difference(count):
    return square_of_sum(count) - sum_of_squares(count)

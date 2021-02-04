import random


def counter(limit=1000):
    for x in range(1, limit+1):
        yield x


def flip_binchar(binarychar):
    return '1' if binarychar == '0' else '0'


def random_event(prob):
    return random.random() < prob

import random


def counter(limit=1000):
    for x in range(1, limit+1):
        yield x


def flip_binchar(binarychar):
    return '1' if binarychar == '0' else '0'


def random_event(prob):
    scale = 10^5
    return random.random() * scale < prob * scale


def printable_at_width(s, width=80):
    if len(s) <= width:
        return s
    else:
        return s[:width] + '\n' + printable_at_width(s[width:], width)



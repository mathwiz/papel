# Condon

import random as rand

def randombase():
    return rand.randint(1,4)


def randomcodon():
    return randombase() * 100 + randombase() * 10 + randombase()


def random():
    return randomcodon()


def validbase(x):
    return x >= 1 and x <=4

def validcodon(x):
    return validbase(int(x / 100)) and validbase(int(x % 100 / 10)) and validbase(int(x % 10))




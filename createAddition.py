import random
from math import ceil as c


def create_addition(result):
    addition_digits = [
        random.randrange(1, c(result)),
        random.randrange(1, c(result))]
    while sum(addition_digits) != result:
        addition_digits = [
            random.randrange(1, c(result / 1.5)),
            random.randrange(1, c(result / 1.5))]
    print(*addition_digits, sep='+')

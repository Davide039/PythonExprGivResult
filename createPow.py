import random
from math import ceil as c


def create_pow(result):
    pow_digits = [
        random.randint(1, c(result)),
        random.randint(1, c(result))]
    while pow_digits[0]**pow_digits[1] != result:
        pow_digits = [
            random.randint(1, c(result)),
            random.randint(1, c(result))]
    print(*pow_digits, sep='^')

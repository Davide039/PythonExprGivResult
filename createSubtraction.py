import random
from math import ceil as c


def create_subtraction(result):
    subtraction_digits = [
        random.randint(1, c(result*3)),
        random.randint(1, c(result))]
    while subtraction_digits[0] - subtraction_digits[1] != result:
        subtraction_digits = [
            random.randint(1, c(result / 0.5)),
            random.randint(1, c(result / 0.5))]
    print(*subtraction_digits, sep='-')

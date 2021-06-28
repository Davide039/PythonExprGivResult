import random
from math import ceil as c


def create_division(result):
    division_digits = [
        random.randint(1, c(result*5)),
        random.randint(1, c(result*5))]
    while division_digits[0] / division_digits[1] != result:
        division_digits = [
            random.randint(1, c(result*5)),
            random.randint(1, c(result*5))]
    print(*division_digits, sep='/')

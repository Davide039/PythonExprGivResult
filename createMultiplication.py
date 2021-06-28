import random
from math import ceil as c


def create_multiplication(result):
    multiplication_digits = [
        random.randint(1, c(result*2)),
        random.randint(1, c(result*2))]
    while multiplication_digits[0] * multiplication_digits[1] != result:
        multiplication_digits = [
            random.randint(1, c(result*2)),
            random.randint(1, c(result*2))]
    print(*multiplication_digits, sep='x')

# -*- coding: utf-8 -*-

import random


def get_non_repeating_random_numbers(a, b, n):
    """
    get non-repeating random numbers(integer)
    :param a: min number
    :param b: max number
    :param n: numbers
    :return: non_repeating random numbers set
    """
    result = set()
    while True:
        result.add(random.randint(a, b))
        if len(result) == n:
            return result


if __name__ == "__main__":
    print(get_non_repeating_random_numbers(1, 13, 4))

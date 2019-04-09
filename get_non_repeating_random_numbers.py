# -*- unicode:utf8 -*-

import random

def get_different_random_int_set(a,b,n):
    result = set()
    while True:
        result.add(random.randint(a,b))
        if len(result) == n:
            return result

if __name__ == "__main__":
	print(get_different_random_int_set(1,13,4))
# -*- coding: utf-8 -*-
from functools import lru_cache

@lru_cache(1)
def add(x, y):
    print("calculating: %s + %s" % (x, y))
    return x + y

if __name__ == '__main__':
    print(add(1, 2))
    # add.cache_clear()
    print(add(1, 2))

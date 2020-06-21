#!/usr/bin/env python3

from functools import wraps
from time import time
import math
import random

# from https://stackoverflow.com/questions/1622943/timeit-versus-timing-decorator

actual_comparisons = 0
comparison_history = {}


def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print('func:%r took: %2.4f sec' % (f.__name__, te-ts))
        return result
    return wrap


@timing
def builtin(inputlist):
    # https://en.wikipedia.org/wiki/Timsort
    return sorted(inputlist)[-2]


def capture_comparison(bigger, smaller):
    if bigger in comparison_history:
        comparison_history[bigger].append(smaller)
    else:
        comparison_history[bigger] = [smaller]


@timing
def second_largest(inputlist):
    return_value = -1
    max_value = compare_even_odd(inputlist)[0]
    for i in comparison_history[max_value]:
        if i > return_value:
            return_value = i
    return return_value


def compare_even_odd(inputlist):
    new_list = []
    if len(inputlist) > 1:
        for i in range(len(inputlist) // 2):
            x = inputlist[2*i]
            y = inputlist[2*i+1]
            max_value = 0
            if x > y:
                max_value = x
                capture_comparison(x, y)
            else:
                max_value = y
                capture_comparison(y, x)

            new_list.append(max_value)

        return compare_even_odd(new_list)
    else:
        return inputlist


def main():
    n = 2**15
    max_comparisons = n + math.log2(n) * n - 2
    inputlist = random.sample(range(n**2), n)
    # use slicing to pass by value
    # print(inputlist)
    expected = builtin(inputlist[:])
    assert second_largest(inputlist) == expected


if __name__ == '__main__':
    main()

#!/usr/bin/env python3

from functools import wraps
from time import time
import numpy as np

# from https://stackoverflow.com/questions/1622943/timeit-versus-timing-decorator


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
    return sorted(inputlist)


@timing
def selection(inputlist):
    returnlist = []
    while len(inputlist) > 0:
        minindex = 0
        for i, _ in enumerate(inputlist):
            if inputlist[i] < inputlist[minindex]:
                minindex = i

        returnlist.append(inputlist.pop(minindex))

    return returnlist


@timing
def bubble(inputlist):
    length = len(inputlist)
    for i in range(length):
        for j in range(i, length):
            if inputlist[i] > inputlist[j]:
                temp = inputlist[i]
                inputlist[i] = inputlist[j]
                inputlist[j] = temp

    return inputlist


@timing
def mergesort(inputlist):
    return merge(inputlist)


def merge(inputlist):
    # based on https://www.geeksforgeeks.org/merge-sort/

    if len(inputlist) > 1:
        # split
        middle = len(inputlist) // 2
        left = inputlist[:middle]
        right = inputlist[middle:]

        merge(left)
        merge(right)

        i = j = k = 0

        # merge lists by stepping through both and finding the smallest element
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                inputlist[k] = left[i]
                i += 1
            else:
                inputlist[k] = right[j]
                j += 1
            k += 1

        # clean up any leftovers
        while i < len(left):
            inputlist[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            inputlist[k] = right[j]
            j += 1
            k += 1

    return inputlist


def main():
    n = 10**4
    inputlist = np.random.randint(n, size=n).tolist()
    # use slicing to pass by value
    expected = builtin(inputlist[:])
    actual = bubble(inputlist[:])
    assert actual == expected
    actual = selection(inputlist[:])
    assert actual == expected
    actual = mergesort(inputlist[:])
    assert actual == expected


if __name__ == '__main__':
    main()

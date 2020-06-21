#!/usr/bin/env python3

from functools import wraps
from time import time

# from https://www.programiz.com/python-programming/examples/multiply-matrix


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
def iterative_approach(x, y):
    # Program to multiply two matrices using nested loops

    # result is 3x4
    result = [[0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]

    # iterate through rows of X
    for i in range(len(x)):
        # iterate through columns of Y
        for j in range(len(y[0])):
            # iterate through rows of Y
            for k in range(len(y)):
                result[i][j] += x[i][k] * y[k][j]

    for r in result:
        print(r)


def main():

    # 3x3 matrix
    x = [[12, 7, 3],
         [4, 5, 6],
         [7, 8, 9]]
    # 3x4 matrix
    y = [[5, 8, 1, 2],
         [6, 7, 3, 0],
         [4, 5, 9, 1]]

    iterative_approach(x, y)


if __name__ == '__main__':
    main()

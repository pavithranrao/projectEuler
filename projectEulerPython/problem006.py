#!/bin/python

import sys


def get_sum_of_n(n):
    return n * (n + 1) / 2


def get_sum_of_n_square(n):
    return (n * (n + 1) * (2 * n + 1)) / 6


def main():
    numInputs = int(raw_input().strip())
    for idx in xrange(numInputs):
        n = int(raw_input().strip())
        answer = get_sum_of_n(n) * get_sum_of_n(n) - get_sum_of_n_square(n)
        print(answer)


if __name__ == '__main__':
    main()

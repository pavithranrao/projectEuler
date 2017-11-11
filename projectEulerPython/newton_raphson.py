#!/usr/bin/python

import sys


def main():
    number = 49
    tolerance = 0.000000001
    x = float(number / 2)
    while (abs((x * x) - number) >= tolerance):
        x = x - ((x * x) - number) / (2 * x)

    print(x)


if __name__ == '__main__':
    main()

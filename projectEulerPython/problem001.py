#!/bin/python

import sys

def getSumOfAP(n, max):
    size = (max - 1) // n
    return (size * (n + size * (n)) / 2)

def getSumOfMultiples(n):
    return (getSumOfAP(3, n) + getSumOfAP(5, n) - getSumOfAP(15, n))

def main():
    numInputs = int(raw_input().strip())
    for idx in xrange(numInputs):
        n = int(raw_input().strip())
        ans = getSumOfAP(n)
        print(ans)

if __name__ == '__main__':
    main()
#!/usr/bin/python

import sys
import math

primes = [2]


def get_all_factors(number):
    factors = []
    for potential_factor in range(1, int(math.sqrt(number)) + 1):
        if number % potential_factor == 0:
            factors.append(potential_factor)
            factors.append(number // potential_factor)
    return factors


def check_prime(number):
    if number == 1:
        return False
    else:
        return len(get_all_factors(number)) == 2


# memoized prime number generator
def get_primes_till_n(n):
    max_prime = max(primes)
    if (max_prime >= n):
        valid_primes = filter(lambda x: x <= n, primes)
        return valid_primes
    else:
        for idx in range(max_prime + 1, n + 1):
            if (check_prime(idx)):
                primes.append(idx)
        return primes


def main():
    # numInputs = int(raw_input().strip())
    # for idx in xrange(numInputs):
    #     n = int(raw_input().strip())

    ans = get_primes_till_n(10)
    print(ans)
    print(primes)
    ans = get_primes_till_n(100)
    print(ans)
    print(primes)
    ans = get_primes_till_n(10)
    print(ans)
    print(primes)


if __name__ == '__main__':
    main()

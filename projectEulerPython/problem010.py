#!/usr/bin/python

import sys

sum_of_primes = [0, 0]


def get_sum_of_primes(n):
    if (n < len(sum_of_primes)):
        return sum_of_primes[n]
    else:
        prime_sieve(n)
        return sum_of_primes[-1]


def prime_sieve(n):
    is_prime = [True] * (n + 1)
    current = 2
    while current * current < n:
        if (is_prime[current]):
            idx = 2
            while idx * current <= n:
                is_prime[idx * current] = False
                idx += 1
        current += 1

    for idx in range(2, n + 1):
        if (idx >= len(sum_of_primes)):
            if (is_prime[idx]):
                sum_of_primes.append(sum_of_primes[-1] + idx)
            else:
                sum_of_primes.append(sum_of_primes[-1])


def main():
    num_of_inputs = int(raw_input().strip())
    for idx in xrange(num_of_inputs):
        n = int(raw_input().strip())
        ans = get_sum_of_primes(n)
        print(ans)


if __name__ == '__main__':
    main()

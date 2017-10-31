import sys
from itertools import count, islice, takewhile

earlier_primes = [2, 3]


# Python 3 Prime implementation with memoization
# Courtesy : https://codereview.stackexchange.com/questions/88012/memoized-prime-generator
def primes():
    yield from earlier_primes
    for n in count(earlier_primes[-1] + 2, 2):
        print('Computing')
        if all(n % p for p in takewhile(lambda p: p**2 <= n, primes())):
            earlier_primes.append(n)
            yield n


def sieve_for_primes_to(n):
    size = n // 2
    sieve = [1] * size
    limit = int(n**0.5)
    max_key = max(memo_map.keys())
    if (n in memo_map):
        return memo_map[n]
    else:
        for i in range(1, limit):
            if sieve[i]:
                val = 2 * i + 1
                tmp = ((size - 1) - i) // val
                sieve[i + val::val] = [0] * tmp
                print(sieve)
        return [2] + [i * 2 + 1 for i, v in enumerate(sieve) if v and i > 0]


def main():
    numInputs = int(raw_input().strip())
    for idx in xrange(numInputs):
        n = int(raw_input().strip())
        ans = sieve_for_primes_to(n)
        print(ans)


if __name__ == '__main__':
    main()

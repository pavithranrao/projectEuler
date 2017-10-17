import sys
import math

def get_all_factors(number):
    factors = []
    for potentialFactors in range(1, int(math.sqrt(number)) + 1):
        if number % potentialFactors == 0:
            factors.append(potentialFactors)
            factors.append(number // potentialFactors)
    return factors

def check_prime(number):
    if number == 1:
        return False
    else:
        return len(get_all_factors(number)) == 2

def get_prime_till_n(n):
    prime = []
    for idx in range(1, n + 1):
        if(check_prime(idx)):
            prime.append(idx)
    return prime

def get_log_base_n(n, b):
    return math.log(n) / math.log(b)

def main():
    print('Hello World!')
    n = 100
    primes = get_prime_till_n(n)
    prod = 1
    for prime in primes:
        max_power = int(get_log_base_n(n, prime))
        print(int(math.pow(prime, max_power)))
        prod = prod * int(math.pow(prime, max_power))

    print(prod)


if __name__ == '__main__':
    main()

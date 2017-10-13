# Compute the largest prime factor for a given number
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

def main():
    input = 600851475143
    all_factors = get_all_factors(input)
    # print(all_factors)

    answer = 0

    for factor in all_factors:
        if (check_prime(factor) and (factor > answer)):
            answer = factor

    print(answer)

if __name__ == '__main__':
    main()

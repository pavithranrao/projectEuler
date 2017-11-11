#!/usr/bin/python

import sys
import math
import itertools

# memoized pythogorean triplets
triplets = {}


def get_all_factors(number):
    factors = []
    for potential_factors in range(1, int(math.sqrt(number)) + 1):
        if number % potential_factors == 0:
            factors.append(potential_factors)
            factors.append(number // potential_factors)
    return factors


#finds if two lists are disjoints
def are_lists_disjoints(a, b):
    return (set(a).isdisjoint(b))


def get_triplets(k):
    if (bool(triplets) and k <= max(triplets.keys())):
        # print('didnt recompute')
        filtered_triplets = {
            key: value
            for key, value in triplets.iteritems() if key <= k
        }
        return filtered_triplets
    else:
        for m in range(1, k):
            for n in range(m + 1, k):
                m_factors = get_all_factors(m)[1:]
                n_factors = get_all_factors(n)[1:]
                if (((n - m) % 2 != 0)
                        and (are_lists_disjoints(m_factors, n_factors))):
                    a = (n * n) - (m * m)
                    b = 2 * m * n
                    c = (m * m) + (n * n)
                    if c > k:
                        break
                    elif (c in triplets):
                        triplets[c].append((a, b))
                    else:
                        triplets[c] = [(a, b)]
        return triplets


def main():

    # num_inputs = int(raw_input().strip())
    # for idx in xrange(num_inputs):
    #     num = int(raw_input().strip())
    #     # num = 12
    #     valid_triplets = get_triplets(num)
    #     # print(valid_triplets)
    #
    #     max_product = -1
    #     for c in valid_triplets:
    #         # k = (num / c)
    #         # print(str(c) + ' => ' + str(num / c))
    #         for triplet in valid_triplets[c]:
    #             # product = math.pow(k, 3) * (c * triplet[0] * triplet[1])
    #             product = c * triplet[0] * triplet[1]
    #             if (product > max_product):
    #                 max_product = product

    num = 1000
    valid_triplets = get_triplets(num)
    # print(valid_triplets)
    print(triplets[425])
    max_product = -1
    for c in valid_triplets:
        # k = (num / c)
        # print(str(c) + ' => ' + str(num / c))
        for triplet in valid_triplets[c]:
            # product = math.pow(k, 3) * (c * triplet[0] * triplet[1])
            product = c * triplet[0] * triplet[1]
            if (product > max_product):
                max_product = product

    print(int(max_product))


if __name__ == '__main__':
    main()

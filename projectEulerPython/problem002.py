import sys

accumulator = {0: 0, 1: 1}
sum_accumulator = {1: 0}

def fib(x):
    if x in accumulator:
        return accumulator[x]
    else:
        f = fib(x - 1) + fib(x - 2)

    accumulator[x] = f
    return f

def get_close_sum(n):
    result = sum_accumulator.keys()[0]
    if (n in sum_accumulator):
        return sum_accumulator[n]
    for i in sum_accumulator.keys():
        if i < n:
            result = i
        if i > n:
            return sum_accumulator[result]


def main():

    # numInputs = int(raw_input().strip())
    numInputs = 4
    sum = 0
    inputs = [100, 610, 10, 0]
    for idx in xrange(numInputs):
        # n = long(raw_input().strip())
        n = inputs[idx]
        last = max(accumulator.values())
        if n <= last:
            # get closest sum
            sum = get_close_sum(n)
        else:
            size = len(accumulator.keys())
            # print(str(n) + ' is greater than computed,' +
            #       ' the last number in fib is : ' + str(last))
            sum = sum_accumulator[max(sum_accumulator.keys())]
            # print('Max sum is : ' + str(sum))
            while last <= n:
                # print('the last element is : ' + str(last))
                last = fib(size + 1)
                if (last % 2 == 0):
                    sum_accumulator[last] = sum + last
                    if (last <= n):
                        sum += last
                size += 1
        # print(sum_accumulator)
        # print(accumulator)
        print(sum)

if __name__ == '__main__':
    main()

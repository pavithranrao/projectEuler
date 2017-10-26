import sys
import math


def getMaxSum(input_list):
    current_max = global_max = input_list[0]
    for idx in range(0, len(input_list)):
        current_max = max(current_max + input_list[idx], input_list[idx])
        if (current_max > global_max):
            global_max = current_max

    return global_max


def getMaxProd(input_list):
    current_max = current_min = global_max = 1
    for idx in range(0, len(input_list)):
        if (input_list[idx] == 0):
            current_max = 1
            current_min = 1
        elif (input_list[idx] > 0):
            current_max = current_max * input_list[idx]
            current_min = min(current_min * input_list[idx], 1)
            global_max = current_max
        else:
            temp = current_max
            current_max = max(current_min * input_list[idx], 1)
            current_min = temp * input_list[idx]
            global_max = max(current_max, current_min)

    return global_max


def main():
    input_list = [-2, -2, -1, 3, 2, 15]
    maxSum = getMaxSum(input_list)
    print(maxSum)

    maxProd = getMaxProd(input_list)
    print(maxProd)


if __name__ == '__main__':
    main()

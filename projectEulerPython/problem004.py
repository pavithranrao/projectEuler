import sys

# product_map = {}
# def get_product_map():
#     for x in range(101, 999):
#         for y in range(101, 999, 100):
#             product = x * y
#             if product in product_map:
#                 temp = product_map[product]
#                 temp.append((x, y))
#                 product_map[product] = temp
#             else:
#                 product_map[product] = [(x, y)]

def check_palindrome(s):
    return (s == s[::-1])

def main():
    # get_product_map()
    # print(len(product_map))
    numInputs = int(raw_input().strip())
    for idx in xrange(numInputs):
        n = int(raw_input().strip())
        i = 101
        j = 101
        greatest = 0
        while (i <= 999):
            while (j <= 999):
                product = i * j
                if (product > greatest
                    and check_palindrome(str(product))
                    and product <= n):
                    greatest = product
                j += 1
            j = 100
            i += 1
        print(greatest)

if __name__ == '__main__':
    main()

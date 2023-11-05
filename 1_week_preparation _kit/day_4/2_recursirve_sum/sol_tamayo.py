
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def sum_digits(num):
    if len(num) == 1:
        return int(num)
    else:
        suma = sum(int(n) for n in num)
        return sum_digits(str(suma))

def superDigit(n, k):
    sum_of_digits = sum(int(digit) for digit in n)
    initial_sum = sum_of_digits * k
    return sum_digits(str(initial_sum))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()

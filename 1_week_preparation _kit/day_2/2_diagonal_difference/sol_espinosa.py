#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#


def diagonalDifference(arr):
    # Write your code here
    def sum_diag(arr):
        len_arr = len(arr)

        if len_arr == 1:
            return arr[0][0]
        else:
            return sum_diag([row[:-1] for row in arr[:-1]]) + arr[-1][-1]

    def sum_antidiag(arr):
        len_arr = len(arr)

        if len_arr == 1:
            return arr[0][0]
        else:
            return sum_antidiag([row[1:] for row in arr[:-1]]) + arr[-1][0]

    return abs(sum_diag(arr) - sum_antidiag(arr))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

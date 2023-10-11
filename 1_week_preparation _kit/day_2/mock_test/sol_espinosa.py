#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#


def flippingMatrix(matrix):
    # Write your code here
    len_submatrix = int(len(matrix) / 2)
    dist = (2 * len_submatrix) - 1

    max_element = []
    for i in range(len_submatrix):
        for j in range(len_submatrix):
            element = matrix[i][j]
            row_hom = matrix[i][dist - j]
            col_hom = matrix[dist - i][j]
            diag_hom = matrix[dist - i][dist - j]

            max_element.append(max(element, row_hom, col_hom, diag_hom))

    return sum(max_element)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        fptr.write(str(result) + '\n')

    fptr.close()

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
    total_max_sum = 0
    matrix_size = len(matrix)
    half_size = matrix_size // 2
    n = matrix_size - 1 # for avoid matrix_size - 1
    
    for row in range(half_size):
        for col in range(half_size):
            
            possible_positions = (
                matrix[row][col],
                matrix[row][n - col],
                matrix[n - row][col],
                matrix[n - row][n - col]
                )
            
            total_max_sum += max(possible_positions)
    
    return total_max_sum
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

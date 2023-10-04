#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    len_arr = len(arr)
    zeros = sum([1 if element == 0 else 0 for element in arr])
    pos = sum([1 if element > 0 else 0 for element in arr])

    zeros_prop = zeros/len_arr
    pos_prop = pos/len_arr
    neg_prop = 1 - (zeros_prop + pos_prop)
    
    print('{:.6f}'.format(pos_prop))
    print('{:.6f}'.format(neg_prop))
    print('{:.6f}'.format(zeros_prop))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

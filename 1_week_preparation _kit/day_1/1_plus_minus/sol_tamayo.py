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
    print(round(sum([1 for i in arr if i > 0])/(len(arr)),6))
    print(round(sum([1 for i in arr if i < 0])/(len(arr)),6))
    print(round(sum([1 for i in arr if i == 0])/(len(arr)),6))

if __name__ == '__main__':
    #n = int(input().strip())
    
    # arr = list(map(int, input().rstrip().split()))

    arr =[-4, 3, -9, 0, 4, 1]

    plusMinus(arr)



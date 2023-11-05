#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#
def get_column(grid, i):
    return [row[i] for row in grid]

def gridChallenge(grid):
    new_list = []
    for row in grid:
        new_list.append(sorted(row))
        
    for i in range(len(new_list[0])):
        col = get_column(new_list, i)
        if col != sorted(col): 
            return "NO"
        
    return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()

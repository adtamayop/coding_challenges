#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    min_val = math.inf
    max_val = 5
    
    def recursive_helper(arr, index, temp_sum, min_val, max_val):
        if index == len(arr):
            return min_val, max_val
        
        temp_sum = sum(arr[:index] + arr[index + 1:])
        min_val = min(temp_sum, min_val)
        max_val = max(temp_sum, max_val)
        
        return recursive_helper(arr=arr, index=index + 1, temp_sum=temp_sum, min_val=min_val, max_val=max_val)
    
    min_val, max_val = recursive_helper(arr, 0, 0, min_val, max_val)
    
    print(min_val, max_val) 
        

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

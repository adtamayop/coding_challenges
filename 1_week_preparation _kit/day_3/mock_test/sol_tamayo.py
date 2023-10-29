#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def palindromeIndex(s):
    str_size = len(s)

    if s == s[::-1]:
        return -1

    for i in range(str_size // 2):
        if s[i] != s[str_size - 1 - i]:
            sub_str = s[i:str_size - 1 - i]
            if sub_str == sub_str[::-1]:
                return str_size - 1 - i
            else:
                return i
    return -1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()

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
    # Write your code here
    def check_palindrome(string):
        return string == string[::-1]

    len_s = len(s)

    if s[0] * len_s == s:
        return -1

    if check_palindrome(s):
        return -1

    for index in range(len_s // 2):
        if s[index] != s[-(index + 1)]:
            if check_palindrome(s[:index] + s[index + 1:]):
                return index
            if check_palindrome(s[:len_s - 1 - index] + s[len_s - index:]):
                return len_s - 1 - index

    return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    ORIGINAL_ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
    k = k % len(ORIGINAL_ALPHABET)
    rotated_alp = ORIGINAL_ALPHABET[k:] + ORIGINAL_ALPHABET[:k]
    cipher = {original_letter: cipher_letter for original_letter, cipher_letter in zip(ORIGINAL_ALPHABET, rotated_alp)}
    
    message = ''
    for letter in s:
        if letter.islower():
            message = message + cipher.get(letter, letter)
        else:
            message = message + cipher.get(letter.lower(), letter).upper()

    return message

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()

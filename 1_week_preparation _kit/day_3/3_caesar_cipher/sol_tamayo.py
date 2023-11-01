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

    k = k % 26

    original_alphabet = "abcdefghijklmnopqrstuvwxyz"
    original_alphabet_list = list(map(str, original_alphabet))
    modified_alphabet_list = list(map(str, (original_alphabet[k:] + original_alphabet[:k])))

    original_alphabet_upper = original_alphabet.upper()
    original_alphabet_upper_list = list(map(str, original_alphabet_upper))
    modified_alphabet_list_upper = list(map(str, (original_alphabet_upper[k:] + original_alphabet_upper[:k])))

    caesar_alphabet = {original_alphabet_list[i]: modified_alphabet_list[i] for i in range(len(original_alphabet))}

    caesar_alphabet_upper = {original_alphabet_upper_list[i]: modified_alphabet_list_upper[i] for i in range(len(original_alphabet))}

    final_alphabet = {**caesar_alphabet, **caesar_alphabet_upper}
    final_string = ""

    for letter in s:
        if final_alphabet.get(letter) is not None:
            final_string += final_alphabet[letter]
        else:
            final_string += letter

    return final_string



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()

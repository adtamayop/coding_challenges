#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    info = s[-2:]
    hour = s[:2]
    additional_info = s[2:-2]
    
    if info == 'AM':
        new_hour = hour if hour != '12' else '00'
    else:
        new_hour = str(int(hour) + 12) if hour != '12' else '12'
        
    return new_hour + additional_info


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()

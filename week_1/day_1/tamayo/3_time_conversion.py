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
    
    hour = int(s[:2])
    complete_hour = s[:-2]

    if s[-2:] == "PM":
        if hour == 12:
            return complete_hour
        else:
            return str(12 + hour) + complete_hour[2:]
    elif s[-2:] == "AM":
        if hour == 12:
            return "00"+ complete_hour[2:]
        else:
            return complete_hour


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    # s = "07:05:45AM"
    # s = "12:00:00PM"

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()

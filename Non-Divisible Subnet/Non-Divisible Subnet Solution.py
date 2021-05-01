#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    # Write your code here
    sDiv=[_%k for _ in s]
    print(sDiv)
    result=0
    if k%2==0:
        if sDiv.count(k%2):
            result+=1
        i=0
    else:
        i=1
    for _ in range (1,k//2+i):
        if sDiv.count(_)>sDiv.count(k-_):
            result+=sDiv.count(_)
        else:
            result+=sDiv.count(k-_)
    if sDiv.count(0):
        result+=1
    return result
    
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()

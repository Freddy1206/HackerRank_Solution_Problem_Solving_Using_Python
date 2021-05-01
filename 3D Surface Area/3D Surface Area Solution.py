#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the surfaceArea function below.
def surfaceArea(A):
    result=0
    for _ in  A:
        result+=sum(_)*6-sum([(i-1)*2 for i in _ if i!=0])-sum([min(_[j],_[j+1])*2   for j in range(len(_)-1)])
    for _ in range(len(A[0])):
        print('\n')
        result-=sum([min(A[i][_],A[i+1][_])*2 for i in range(len(A)-1)])
        print(result)
    return result

if '__name__' == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    HW = input().split()

    H = int(HW[0])

    W = int(HW[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    fptr.write(str(result) + '\n')

    fptr.close()

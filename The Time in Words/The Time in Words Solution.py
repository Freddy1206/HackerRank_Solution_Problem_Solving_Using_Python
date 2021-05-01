#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the timeInWords function below.
def timeInWords(h, m):
    number=('one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','quarter','sixteen','seventeen','eighteen','nineteen','twenty','twenty one','twenty two','twenty three','twenty four','twenty five','twenty six','twenty seven','twenty eight','twenty nine','half')
    if m==0:
        if h==0:
            return 'twelve o\' clock'
        return number[h-1]+ ' o\' clock'
    elif m<=30:
        if m==15 or m==30:
            return number[m-1] +' past '+ number[h-1]
        elif m==1:
            return number[m-1] +' minute past '+ number[h-1]
        return number[m-1] +' minutes past '+ number[h-1]
    else:
        if h==12:
            if m==15:
                return number[60-m-1]+' to '+number[0]
            elif m==1:
                return number[60-m-1]+' minute to '+number[0]
            return number[60-m-1]+' minutes to '+number[0]
        else:
            if m==30 or m==45:
                return number[60-m-1]+' to '+number[h]
            elif m==1:
                return number[60-m-1]+' minute to '+number[h]
            return number[60-m-1]+' minutes to '+number[h]
if '__name__' == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()

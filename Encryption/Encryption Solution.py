#!/bin/python3

import math as m
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    s=''.join(s.strip().split())
    lenght=m.ceil(m.sqrt(len(s)))
    print(lenght)
    result=''
    for _ in range(lenght):
        data=''
        for i in range(_,len(s),lenght):
            data+=s[i]
        result+=data +' '
    return result.strip()
        
if '__name__' == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obst):
    obstacles = {(ob[0],ob[1]) for ob in obst}

    mvs, count = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(-1,1),(1,-1)], 0

    for m in mvs:
        cr, cc = r_q, c_q
        while (cr + m[0] >= 1 and cr + m[0] <= n) and (cc + m[1] >= 1 and cc + m[1] <= n):
            cr += m[0]
            cc += m[1]
            if (cr, cc) in obstacles:break
            count += 1

    return count
                    
if '__name__' == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()

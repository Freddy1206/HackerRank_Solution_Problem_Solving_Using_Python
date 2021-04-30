#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bomberMan function below.
def bomberMan(n, grid,r,c):
    if n==1:
        return grid
    elif n%2==0:
        return ['O'*c for _ in range (r)]
    
    grid1=[['O']*c for _ in range(r)]
    grid2=[['O']*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if grid[i][j]=='O':
              for j in range(c):
            if grid1[i][j]=='O':
                grid2[i][j]='.'
                if i-1>=0:
                    grid2[i-1][j]='.'
                if i+1<r:
                    grid2[i+1][j]='.'
                if j-1>=0:
                    grid2[i][j-1]='.'
                if j+1<c:
                    grid2[i][j+1]='.'
    grid1=[''.join(_) for _ in grid1]
    grid2=[''.join(_) for _ in grid2]
    if (n-3)%4==0:
        return grid1
    return grid2          grid1[i][j]='.'
                if i-1>=0:
                    grid1[i-1][j]='.'
                if i+1<r:
                    grid1[i+1][j]='.'
                if j-1>=0:
                    grid1[i][j-1]='.'
                if j+1<c:
                    grid1[i][j+1]='.'
    for i in range(r):

                        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    rcn = input().split()

    r = int(rcn[0])

    c = int(rcn[1])

    n = int(rcn[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid,r,c)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()

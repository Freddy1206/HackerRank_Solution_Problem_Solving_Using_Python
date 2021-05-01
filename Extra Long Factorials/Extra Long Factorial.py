#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the extraLongFactorials function below.
def extraLongFactorials(n):
    return n * extraLongFactorials(n-1) if n>1 else 1
if __name__ == '__main__':
    n = int(input())

    print(extraLongFactorials(n))

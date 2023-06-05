#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#

def formingMagicSquare(s):
    # Write your code here
    msp = {
    0:[8,1,6,3,5,7,4,9,2],
    1:[6,1,8,7,5,3,2,9,4],
    2:[4,9,2,3,5,7,8,1,6],
    3:[2,9,4,7,5,3,6,1,8],
    4:[8,3,4,1,5,9,6,7,2],
    5:[4,3,8,9,5,1,2,7,6],
    6:[6,7,2,1,5,9,8,3,4],
    7:[2,7,6,9,5,1,4,3,8],
    }

    box = [*s[0], *s[1], *s[2]]

    result = [0, 0, 0, 0, 0, 0, 0, 0]

    for x in range(9):
            result[0] += abs(msp[0][x] - box[x])
            result[1] += abs(msp[1][x] - box[x])
            result[2] += abs(msp[2][x] - box[x])
            result[3] += abs(msp[3][x] - box[x])
            result[4] += abs(msp[4][x] - box[x])
            result[5] += abs(msp[5][x] - box[x])
            result[6] += abs(msp[6][x] - box[x])
            result[7] += abs(msp[7][x] - box[x])
    return min(result)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()


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
    if "P" in s:
        S=s.replace('PM', '')
        new_list = S.split(":")
        x = int(new_list[0])
        y = new_list[1]
        z = new_list[2]
        if x < 12:
           x+=12
        new_string = f'{x}:{y}:{z}' 
        return new_string  
    else:
        S=s.replace('AM', '')
        new_list = S.split(":")
        x = new_list[0]
        y = new_list[1]
        z = new_list[2]
        if x == "12":
           x = "00"
        new_string = x+":"+y+":"+z
        return new_string  
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()

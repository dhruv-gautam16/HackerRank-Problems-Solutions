#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    a_sum=0
    b_sum=0
    n=len(a)
    for i in range(n):
        if a[i]>b[i]:
            a_sum+=1
        elif b[i]>a[i]:
            b_sum+=1
        else:
            continue
    d=[]
    d.append(a_sum)
    d.append(b_sum)
    return d
        

if __name__ == '__main__':
    

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    n=len(result)
    for i in range(n):
        print(result[i],end=' ')
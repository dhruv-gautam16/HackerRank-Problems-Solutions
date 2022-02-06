#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'angryProfessor' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY a
#



if __name__ == '__main__':
    
    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        a = list(map(int, input().rstrip().split()))
        pos=0
        neg=0
        for i in a:
            if i>0:
                pos+=1
            elif(i<=0):
                neg+=1
        if(k<=neg):
            print("NO")
        else:
            print("YES")
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#


def staircase(num_stairs):
    for stairs in range(1, num_stairs + 1):
        print(' ' * (num_stairs - stairs) + '#' * stairs)
if __name__ == '__main__':
    num_stairs = int(input().strip())

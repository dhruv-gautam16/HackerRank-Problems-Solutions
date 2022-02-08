#!/bin/python3

import sys


s,n,m = [int(x) for x in input().strip().split(' ')]
keyboards = [int(keyboards_temp) for keyboards_temp in input().strip().split(' ')]
pendrives = [int(pendrives_temp) for pendrives_temp in input().strip().split(' ')]

total = -1

for x in keyboards:
    for y in pendrives:
        z = x + y
        if z > total and z <= s:
            total = z
         
print(total)
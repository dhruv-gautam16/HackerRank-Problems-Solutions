#!/bin/python3

import sys


n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]
acc = 0
for i, e in enumerate(a):
    for j in range(i+1, len(a)):
        acc += (e + a[j]) % k == 0
print(acc)

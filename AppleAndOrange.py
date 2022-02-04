#!/bin/python3

import sys


s,t = input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = input().strip().split(' ')
a,b = [int(a),int(b)]
#print(a)
#print(b)
m,n = input().strip().split(' ')
m,n = [int(m),int(n)]
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]
countA = 0;
countO = 0;
for i in apple:
    if(i + a >= s and i + a <= t):
        countA += 1

for j in orange:
    if(j + b >= s and j + b <= t):
        countO += 1    

print(countA)

print(countO)
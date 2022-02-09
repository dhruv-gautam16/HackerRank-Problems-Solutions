def odd(n):
    return ((n % 2) == 1)

def even(n):
    return ((n % 2) == 0)

def utopia(n):
    if n == 0:
        return 1
    elif odd(n):
        return 2 * utopia(n-1)
    elif even(n):
        return 1 + utopia(n-1)
    

t = int(input())

for i in range(0, t):
    n = int(input())
    print(utopia(n))
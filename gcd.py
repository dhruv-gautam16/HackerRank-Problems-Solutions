def gcd(x,y):
    if y==0:
        return x
    else:
        return gcd(y,x%y)

x,y=map(int,input().split())

d=gcd(x,y)

print(d)
n=int(input())
a=[]
for i in range(n):
    s=str(input())
    a.append(s)
d=set(a)
e=list(d)
print(len(e))
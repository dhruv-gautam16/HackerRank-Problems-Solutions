n = int(input())
s = list(map(int, input().split()))
d, m = map(int, input().split())
ans = 0
for i in range(n-m+1):
    if (sum(s[i:i+m]) == d):
        ans += 1
        
print(ans)
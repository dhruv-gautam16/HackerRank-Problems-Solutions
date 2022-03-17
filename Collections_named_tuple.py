N, headers, total = int(input()), list(input().split()), 0
for _ in range(N):
    total += int(list(input().split())[headers.index('MARKS')])
print(total/N)
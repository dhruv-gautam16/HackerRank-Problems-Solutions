import re
t = int(input())
for _ in range(t):
    try:
        re.compile(input())
        print(True)
    except re.error:
        print(False)
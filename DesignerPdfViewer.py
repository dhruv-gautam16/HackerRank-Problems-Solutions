

import sys
import string

h = [int(h_temp) for h_temp in input().strip().split(' ')]
word = input().strip()

w_len = len(word)
st = string.ascii_lowercase
max_h = 0

for ch in word:
    i = st.index(ch)
    max_h = max(max_h, h[i])

ans = max_h*w_len

print(ans)
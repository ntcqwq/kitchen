from collections import deque, defaultdict as dd, Counter
from bisect import bisect_left as bs
import sys, math, heapq as hq, itertools, copy
input, inf, mx = sys.stdin.readline, 1e30, int(1e6)+2 
# sys.setrecursionlimit(100000)

s = input().strip()
N = len(s)
psaa = [0] * (N+1)
psab = [0] * (N+1)
for i in range(N):
    psaa[i+1] = psaa[i]
    psab[i+1] = psab[i]
    if s[i] == 'A':
        psaa[i+1] += 1
    elif s[i] == 'B':
        psab[i+1] += 1
a = psaa[-1]
b = psab[-1]
ans = inf
for i in range(N-a+1):
    ans = min(ans, a-(psaa[i+a]-psaa[i]))
for i in range(N-b+1):
    ans = min(ans, b-(psab[i+b]-psab[i]))
print(ans)
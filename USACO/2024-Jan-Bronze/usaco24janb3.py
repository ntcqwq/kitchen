from collections import deque, defaultdict; from bisect import bisect_left as bs; import sys, math, heapq as hq, itertools, copy;
input, inf, mx = sys.stdin.readline, 1e30, 102 
# sys.setrecursionlimit(100000)
    
N = int(input())
g = list(map(int, input().split()))
b = -g[0]
ans = abs(g[0])
t = -g[0]
for i in range(1, N):
    t += b
    b -= g[i]+t
    ans += abs(g[i]+t)
    t -= g[i]+t
print(ans)
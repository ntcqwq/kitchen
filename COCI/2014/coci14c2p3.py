from collections import deque; from bisect import bisect_right as bs; import sys, math, heapq as hq;
input, inf, mx = sys.stdin.readline, float('inf'), 2010
# sys.setrecursionlimit(100000)

N, K = map(int, input().split())
v = list(map(int, input().split()))
a = sorted([[v[i], i] for i in range(N)])
g = [0] * N
for i in range(N):
    g[a[i][1]] = i//K
lis = []
for i in range(N):
    x = g[i]
    if not lis or x >= lis[-1]:
        lis.append(x)
    else:
        lis[bs(lis, x)] = x
print(N-len(lis))
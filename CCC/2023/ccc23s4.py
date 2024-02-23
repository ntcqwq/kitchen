from collections import deque, defaultdict 
from bisect import bisect_left as bs
import sys, math, heapq as hq, itertools, copy
input, inf, mx, mod = sys.stdin.readline, 1e30, 302, 1000000007
# sys.setrecursionlimit(100000)

def find(n):
    if n != ds[n]:
        ds[n] = find(ds[n])
    return ds[n]

def merge(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return
    else:
        ds[a] = b

N, M = map(int, input().split())
edges = []
ds = [i for i in range(N+1)]

for _ in range(M):
    u, v, l, c = map(int, input().split())
    edges.append([c, u, v])

edges.sort()
# kruskal

ans = 0
for d, a, b in edges:
    fa = find(a)
    fb = find(b)
    if fa != fb:
        ds[fa] = fb
        ans += d

print(ans)
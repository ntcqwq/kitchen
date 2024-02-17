from collections import deque
from bisect import bisect_left as bs
import sys, math
import heapq as hq

# sys.setrecursionlimit(100000)

input = sys.stdin.readline

K, N, M = map(int, input().split())

adjl = [[] for _ in range(N+1)]
dis = [[float('inf')] * (K+1) for _ in range(N+1)]

for _ in range(M):
    a, b, t, h = map(int, input().split())
    adjl[a].append((b, t, h))
    adjl[b].append((a, t, h))

A, B = map(int, input().split())

q = [(0, A, 0)] 
dis[A][0] = 0

while q:
    d, a, h = hq.heappop(q)
    if d > dis[a][h]:
        continue
    if a == B:
        print(d)
        sys.exit()
    for b, t, nh in adjl[a]:
        ch = h + nh
        if ch < K and dis[b][ch] > dis[a][h] + t:
            dis[b][ch] = dis[a][h] + t
            hq.heappush(q, (dis[b][ch], b, ch))

print(-1)
from collections import deque, defaultdict 
from bisect import bisect_left as bs
import sys, math, heapq as hq, itertools, copy
input, inf, mx, mod = sys.stdin.readline, 1e30, 302, 1000000007
# sys.setrecursionlimit(100000)

def dijkstra(a, b):
    dis = [inf] * (N+1)
    dis[a] = 0
    q = [[0, a]]
    while q:
        d, u = hq.heappop(q)
        if u == b:
            break
        for l, v in adjl[u]:
            if dis[u] + l < dis[v]:
                dis[v] = dis[u] + l
                hq.heappush(q, [dis[v], v])
    return dis[b]

N, M = map(int, input().split())
edges = []
ds = [i for i in range(N+1)]
adjl = [[] for _ in range(N+1)]

for _ in range(M):
    u, v, l, c = map(int, input().split())
    edges.append([l, c, u, v])
    
edges.sort()

ans = 0
for l, c, a, b in edges:
    d1 = dijkstra(a, b)
    adjl[a].append([l, b])
    adjl[b].append([l, a])
    d2 = dijkstra(a, b)
    if d2 < d1:
        ans += c
    else:
        adjl[a].pop()
        adjl[b].pop()
print(ans)
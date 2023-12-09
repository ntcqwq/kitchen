from collections import deque
from bisect import bisect_left as bs
import sys, math
 
input = sys.stdin.readline
 
N = int(input())
T = int(input())
 
adjl = [[0]*(N+1) for _ in range(N + 1)]
cost = [-1] * (N + 1)
 
for _ in range(T):
    a, b, w = map(int, input().split())
    adjl[a][b] = adjl[b][a] = w
 
K = int(input())
for _ in range(K):
    z, c = map(int, input().split())
    cost[z] = c
 
D = int(input())
 
dis = [float('inf')] * (N + 1)
vis = [False] * (N + 1)
dis[D] = 0
for k in range(N):
    mi, u = float('inf'), -1
    for i in range(1, N+1):
        if not vis[i] and dis[i] < mi:
            mi, u = dis[i], i
    vis[u] = True
    for v in range(1, N+1):
        if adjl[u][v] != 0 and dis[v] > dis[u] + adjl[u][v]:
            dis[v] = dis[u] + adjl[u][v]
 
ans = float('inf')
for i in range(1, N + 1):
    if cost[i] != -1:
        ans = min(ans, dis[i] + cost[i])
 
print(ans)
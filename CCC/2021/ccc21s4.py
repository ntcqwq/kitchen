from collections import deque
from bisect import bisect_left as bs
from itertools import permutations
import sys, math
import heapq as hq

# sys.setrecursionlimit(100000)

input = sys.stdin.readline
inf = float('inf')

N, W, D = map(int, input().split())

adjl = [[] for _ in range(N+1)]

for _ in range(W):
    a, b = map(int, input().split())
    adjl[b].append(a)

walkways = [inf] * (N+1)

q = deque([N])
walkways[N] = 0
while q:
    a = q.popleft()
    for b in adjl[a]:
        if walkways[b] == inf:
            walkways[b] = walkways[a] + 1
            q.append(b)

train = [0] * (N+1)
s = [0] + list(map(int, input().split()))
pq = []

for i, station in enumerate(s):
    train[station] = i
    hq.heappush(pq, (walkways[station] + train[station], station))


for i in range(1, N+1):
    hq.heappush(pq, (train[i] + walkways[i], i))


for _ in range(D):
    x, y = map(int, input().split())
    s[x], s[y] = s[y], s[x]
    train[s[x]], train[s[y]] = train[s[y]], train[s[x]]
    hq.heappush(pq, (train[s[x]] + walkways[s[x]], s[x]))
    hq.heappush(pq, (train[s[y]] + walkways[s[y]], s[y]))
    while 1:
        time, station = pq[0]
        if time == walkways[station] + train[station]:
            print(time-1)
            break
        hq.heappop(pq)
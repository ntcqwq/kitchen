# https://dmoj.ca/problem/ccc14s5
# 90/150 Python 3

import sys
N = int(sys.stdin.readline())

pts = [[0, 0]]
for i in range(N):
    pt = input().split()
    pts.append([int(pt[0]), int(pt[1])])

pairs = []
for a in range(N+1):
    for b in range(a+1, N+1):
        dx = pts[a][0] - pts[b][0]
        dy = pts[a][1] - pts[b][1]
        pairs.append([dx * dx + dy * dy, a, b])

pairs.sort()

best  = [0] * (N+1)
pbest = [0] * (N+1)
pdist = [0] * (N+1)

for pair in pairs:
    d = pair[0]
    a = pair[1]
    b = pair[2]

    if d != pdist[a]:
        pdist[a] = d
        pbest[a] = best[a]
    if d != pdist[b]:
        pdist[b] = d
        pbest[b] = best[b]

    if a == 0: 
        best[a] = max(best[a], pbest[b])
    else:
        best[a] = max(best[a], pbest[b] + 1)
        best[b] = max(best[b], pbest[a] + 1)    

print(best[0] + 1)
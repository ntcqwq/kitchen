from collections import deque
from bisect import bisect_left as bs
from itertools import permutations
import sys, math
import heapq as hq

# sys.setrecursionlimit(100000)

input = sys.stdin.readline
inf = float('inf')

N, M = map(int, input().split())

camq = deque([])
q = deque([])
vis = [[False]*M for _ in range(N)]
dis = [[-1]*M for _ in range(N)]

grid = [['']*M for _ in range(N)]
d = [(0, -1), (0, 1), (-1, 0), (1, 0)]
cv = ['L', 'R', 'U', 'D']

for r in range(N):
    cells = list(input().strip())
    for c in range(M):
        if cells[c] == 'C':
            camq.append((r, c, -1))
            vis[r][c] = True
        elif cells[c] == 'S':
            q.append((r, c))
            dis[r][c] = 0
        grid[r][c] = cells[c]

while camq:
    a, b, di = camq.popleft()
    if di == -1:
        for i in range(4):
            na, nb = a + d[i][0], b + d[i][1]
            if 0 <= na < N and 0 <= nb < M:
                if grid[na][nb] != 'W':
                    camq.append((na, nb, i))
                    vis[na][nb] = True
    else:
        na, nb = a + d[di][0], b + d[di][1]
        if 0 <= na < N and 0 <= nb < M:
            if grid[na][nb] != 'W':
                camq.append((na, nb, di))
                vis[na][nb] = True

if not vis[q[0][0]][q[0][1]]:
    while q:
        a, b = q.popleft()
        if grid[a][b] in cv:
            for di in range(4):
                if grid[a][b] == cv[di]:
                    nna, nnb = a + d[di][0], b + d[di][1]
                    if 0 <= nna < N and 0 <= nnb < M:
                        if not vis[nna][nnb] and grid[nna][nnb] != 'W' and (dis[nna][nnb] == -1 or dis[nna][nnb] > dis[a][b]):  
                            dis[nna][nnb] = dis[a][b]
                            q.appendleft((nna, nnb))
        else:
            for y, x in d:
                na, nb = a + y, b + x
                if 0 <= na < N and 0 <= nb < M:
                    if dis[na][nb] == -1 or dis[na][nb] > dis[a][b] + 1:
                        if grid[na][nb] != 'W':
                            for di in range(4):
                                if grid[na][nb] == cv[di]:
                                    dis[na][nb] = dis[a][b] + 1
                                    nna, nnb = na + d[di][0], nb + d[di][1]
                                    if 0 <= nna < N and 0 <= nnb < M:
                                        if not vis[nna][nnb] and grid[nna][nnb] != 'W' and dis[nna][nnb] == -1:  
                                            dis[nna][nnb] = dis[na][nb]
                                            q.appendleft((nna, nnb))
                            else:
                                if not vis[na][nb]:
                                    dis[na][nb] = dis[a][b] + 1
                                    q.append((na, nb))

for r in range(N):
    for c in range(M):
        if grid[r][c] == '.':
            print(dis[r][c])


'''
4 3
CRR
USD
WWU
..L
'''
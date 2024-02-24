from collections import deque, defaultdict; from bisect import bisect_left as bs; import sys, math, heapq as hq, itertools, copy;
input, inf, mx = sys.stdin.readline, 1e30, 102 
# sys.setrecursionlimit(100000)

N, cur = map(int, input().split())
ans, power, dr, a = 0, 1, 1, 0
last = inf
l = []
vis = [0]*N
for _ in range(N):
    q, v = map(int, input().split())
    l.append([q, v])
    if q == 1:
        a += 1
cur -= 1
while True:
    if l[cur][0] == 1:
        if power >= l[cur][1] and l[cur][1] != -1:
            ans += 1
            l[cur][1] = -1
            a -= 1
        if vis[cur] == last:
            break
        vis[cur] = last
    elif l[cur][0] == 0:
        dr ^= 1
        power += l[cur][1]
        if vis[cur] == last:
            break
        vis[cur] = last
    last = cur
    if dr == 0:
        cur -= power
    elif dr == 1:
        cur += power
    if cur < 0 or cur > N-1 or a == 0:
        break
print(ans)
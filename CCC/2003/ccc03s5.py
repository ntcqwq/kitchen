# CCC '03 S5 - Trucking Troubles
# Ideas: Disjoint Sets

from collections import deque
import sys
input = sys.stdin.readline

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


N, M, D = map(int, input().split())
edge = sorted([list(map(int, input().split())) for _ in range(M)], key = lambda x: x[2], reverse = True)
ds = [i for i in range(N+1)]
des = [int(input()) for _ in range(D)]

i = 0
ans = 0
for v in des:
    while find(1) != find(v):
        a, b, w = edge[i]
        fa = find(a)
        fb = find(b)
        if fa != fb:
            ds[fa] = fb
            ans = w
        i += 1
print(ans)
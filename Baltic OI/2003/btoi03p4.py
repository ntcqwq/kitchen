from collections import deque
import sys

input = sys.stdin.readline

def find(n, par):
    if n != par[n]:
        par[n] = find(par[n], par)
    return par[n]

def merge(a, b, ds):
    a = find(a, ds)
    b = find(b, ds)
    if a == b:
        return
    else:
        ds[a] = b

N = int(input())
M = int(input())

ds = list(range(N+1))
ds.extend(list(range(N+1, 2*N+1)))

for _ in range(M):
    f, p, q = input().split()
    p, q = int(p), int(q)
    if f == 'F':
        merge(p, q, ds)
    elif f == 'E':
        merge(q+N, p, ds)
        merge(p+N, q, ds)

gangs = set()

for i in range(1, N+1):
    gangs.add(find(i, ds))
    
print(len(gangs))
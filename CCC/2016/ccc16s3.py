from collections import deque
import sys;
input = sys.stdin.readline;
sys.setrecursionlimit(100000);

N, M = map(int, input().split());
pho = [False] * N;
nodes = 0;
ms = input().split()
for x in ms:
    pho[int(x)] = True;

far, end = 0, 0;

adjl = [[] for _ in range(N)];
for _ in range(N-1):
    a, b = map(int, input().split());
    adjl[a].append(b);
    adjl[b].append(a);

def dfs(y, p):
    global nodes;
    for a in adjl[y]:
        if a != p:
            dfs(a, y);
            if pho[a]:
                pho[y] = True;
    nodes += pho[y]

dfs(int(ms[0]), -1);

def dfs2(y, p, d):
    global far, end;
    if d > far:
        far = d;
        end = y;
    for a in adjl[y]:
        if a != p and pho[a]:
            dfs2(a, y, d+1);

dfs2(int(ms[0]), -1, 0);
dfs2(end, -1, 0);
diameter = far;
print(2*(nodes-1)-diameter)

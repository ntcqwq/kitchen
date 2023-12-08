from collections import deque;
from copy import copy;
import sys;

input = sys.stdin.readline;

N = int(input());

adjl = {};
r = {};

for i in range(N):
    a, b = map(int, input().split());
    r[a] = -1;
    adjl[a] = b;

while True:
    a, b = map(int, input().split());
    if a | b == 0:
        break;
    dis = copy(r);
    q = deque([a]);
    ans = "No";
    while q:
        y = q.popleft();
        if y == b:
            ans = f"Yes {dis[y]}";
            break;
        if dis[adjl[y]] == -1:
            q.append(adjl[y]);
            dis[adjl[y]] = dis[y] + 1;
    print(ans);
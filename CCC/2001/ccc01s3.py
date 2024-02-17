from collections import deque;
import sys;

input = sys.stdin.readline;

adjl = [[] for _ in range(26)];
edges = [];

c = lambda x: ord(x) - 65;
t = lambda x: chr(x+65);

while True:
    a, b = map(c, input().strip());
    if a == -23:
        break;
    adjl[a].append(b);
    adjl[b].append(a);
    edges.append((a, b));

ans = 0;

for a, b in edges:
    vis = [0] * 26;
    q = deque([0]);
    while q:
        y = q.popleft();
        for n in adjl[y]:  
            if vis[n] == 0 and (y != a or n != b) and (n != a or y != b):
                q.append(n);
                vis[n] = 1;
    if vis[1] == 0:
        ans += 1;
        print(f"{t(a)}{t(b)}")

print(f"There are {ans} disconnecting roads.")

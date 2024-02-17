from collections import deque
import sys

input = sys.stdin.readline

d = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)];

A, B = map(int, input().split());
C, D = map(int, input().split());


q = deque([(A-1, B-1)]);
dis = [[-1]*8 for _ in range(8)];
dis[A-1][B-1] = 0
while q:
    x, y = q.popleft();
    if (x, y) == (C-1, D-1):
        print(dis[x][y]);
        break;
    for na, nb in d:
        nx, ny = x+na, y+nb;
        if 0 <= nx < 8 and 0 <= ny < 8 and dis[nx][ny] == -1:
            q.append([nx, ny]);
            dis[nx][ny] = dis[x][y] + 1;

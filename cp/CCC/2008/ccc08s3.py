from collections import deque;
import sys;

input = sys.stdin.readline;

T = int(input());

d1 = [(1, 0), (0, 1), (-1, 0), (0, -1)];
d2 = [(-1, 0), (1, 0)];
d3 = [(0, 1), (0, -1)];

for _ in range(T):
    R, C = int(input()), int(input());
    grid = [list(input().strip()) for _ in range(R)];

    start = (0, 0);
    end = (C-1, R-1);

    q = deque([start]);
    dis = [[-1] * C for _ in range(R)];
    dis[start[0]][start[1]] = 0;

    m = 0;

    while q:
        x, y = q.popleft();
        if (x, y) == end:
            print(dis[y][x] + 1);
            break;
        d = [];
        if grid[y][x] == "+":
            d = d1;
        elif grid[y][x] == "-":
            d = d2;
        elif grid[y][x] == "|":
            d = d3;
        for na, nb in d:
            nx, ny = x + na, y + nb;
            if 0 <= nx < C and 0 <= ny < R:
                if dis[ny][nx] == -1:
                    if grid[ny][nx] != '*':
                        q.append([nx, ny]);
                        dis[ny][nx] = dis[y][x] + 1;
    else:
        print(-1);
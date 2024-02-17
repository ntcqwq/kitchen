from collections import deque;
import sys;

input = sys.stdin.readline;

N = int(input());

flowers = [[int(x) for x in input().strip().split()] for _ in range(N)];

for i in range(0, 4):
    f = True;
    for i in range(N):
        if flowers[i] == sorted(flowers[i]):
            for j in range(N):
                if flowers[-1][j] > flowers[0][j]:
                    f = False;
                else:
                    f = True;
                    break;

    if not f:
        for y in range(N):
            for x in range(N):
                print(flowers[y][x], end=" ")
            print()

    flowers = list(zip(*flowers[::-1]))
    flowers = [list(i) for i in flowers]
'''
grid[x][y] --> grid[y][N-1-x]

N: grid size
2x2 N=2
'''
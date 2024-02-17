from collections import deque
from bisect import bisect_left as bs
from itertools import permutations
import sys, math
import heapq as hq

# sys.setrecursionlimit(100000)

input = sys.stdin.readline
inf = 32+1

r, c = map(int, input().split())
k = int(input())
cat = [[False] * (inf) for _ in range(inf)]
dp = [[0] * (inf) for _ in range(inf)]

for _ in range(k):
    x, y = map(int, input().split())
    cat[x][y] = True

dp[1][1] = 1

for i in range(1, r + 1):
    for j in range(1, c + 1):
        if not cat[i][j]:
            if i != 1:
                dp[i][j] += dp[i - 1][j]
            if j != 1:
                dp[i][j] += dp[i][j - 1]

print(dp[r][c])
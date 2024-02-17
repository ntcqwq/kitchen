from collections import deque; from bisect import bisect_left as bs; import sys, math, heapq as hq;
input, inf = sys.stdin.readline, float('inf')
# sys.setrecursionlimit(100000)

N = int(input())
K = int(input())
dp = [[0]*(K+1) for _ in range(N+1)]
def pi(i, j):
    if i == 0 and j != 0:
        return 1
    if i < 0 or (i != 0 and j == 0):
        return 0
    if dp[i][j]:
        return dp[i][j]
    dp[i][j] = pi(i, j-1) + pi(i-j, j)
    return dp[i][j]
print(pi(N-K, K))
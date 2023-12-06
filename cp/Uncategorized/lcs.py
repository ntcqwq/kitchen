from collections import deque; from bisect import bisect_left as bs; import sys, math, heapq as hq;
input, inf = sys.stdin.readline, float('inf')
# sys.setrecursionlimit(100000)

N = int(input())
K = int(input())

dp = [[[0]*(N+1) for _ in range(K+1)] for _ in range(N+1)]
if dp[N][K][1] == 0:
    if N == K or K == 1:
        
    else:
        t = 0
        for i in range(min, int((n/k)+1)):
            t = t + pi(n-i, k-1, i)
        visited[n][k][min] = t
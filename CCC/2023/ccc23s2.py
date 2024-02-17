from collections import deque; from bisect import bisect_left as bs; import sys, math, heapq as hq, itertools, copy;
input, inf, mx = sys.stdin.readline, float('inf'), 2*int(1e10)
# sys.setrecursionlimit(100000)

N = int(input())
m = list(map(int, input().split()))
dp = [[0] * (N+1) for _ in range(N+1)]
ans = [mx] * N
ans[0] = 0
for i in range(1, N):
    for l in range(1, N+1-i):
        r = l+i
        dp[l][r] = dp[l+1][r-1] + abs(m[l-1]-m[r-1])
        ans[i] = min(ans[i], dp[l][r])
print(*ans)
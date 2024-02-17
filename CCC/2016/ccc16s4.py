from collections import deque; from bisect import bisect_left as bs; import sys, math, heapq as hq;
input, inf, mx = sys.stdin.readline, float('inf'), int(4e14)
# sys.setrecursionlimit(100000)

N = int(input())
r = list(map(int, input().split()))
dp = [[0]*(N+1) for _ in range(N+1)]
psa = [0] * (N+1)
ans = 0
for i in range(1, N+1):
    psa[i] = psa[i-1] + r[i-1]
    dp[i][i] = 1
    ans = max(ans, r[i-1])
for i in range(1, N):
    for l in range(1, N-i+1):
        r = l+i
        for m in range(l, r):
            if dp[l][m] and dp[m+1][r] and psa[m]-psa[l-1] == psa[r]-psa[m]:
                dp[l][r] = 1
        lb, ub = 1, N
        while lb < ub:
            if dp[l][lb] and dp[lb+1][ub-1] and dp[ub][r] and psa[lb]-psa[l-1] == psa[r]-psa[ub-1]:
                dp[l][r] = 1
                break
            elif psa[lb]-psa[l-1] < psa[r]-psa[ub-1]:
                lb += 1
            else:
                ub -= 1
        if dp[l][r]:
            ans = max(ans, psa[r]-psa[l-1])
print(ans)
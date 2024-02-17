from collections import deque
from bisect import bisect_left as bs
import sys, math
import heapq as hq

# sys.setrecursionlimit(100000)

input = sys.stdin.readline

n, m, k = map(int, input().split())
ans = []

for i in range(n):
    rem = n - i - 1
    cur = min(k - rem, m)
    if cur <= 0:
        break
    val = 0
    if cur > i:
        val = min(m, i + 1)
        cur = val
    else:
        val = ans[i - cur]
    ans.append(val)
    k -= cur

if k == 0 and len(ans) == n:
    print(*ans)
else:
    print(-1)
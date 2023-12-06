from collections import deque
from bisect import bisect_left as bs
import sys, math
import heapq as hq

# sys.setrecursionlimit(100000)

input = sys.stdin.readline
inf = float('inf')

T = int(input())
for _ in range(T):
    N = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = []
    if N % 2:
        print(*a)
    elif a[0] == a[-1]:
        print(-1)
    else:
        f = a[0:N//2]
        s = a[N//2:N]
        for a, b in zip(f, s):
            ans.append(a)
            ans.append(b)
        print(*ans)
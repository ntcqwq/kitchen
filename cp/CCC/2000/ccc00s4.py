from collections import deque
from bisect import bisect_left as bs
from itertools import permutations
import sys, math
import heapq as hq

# sys.setrecursionlimit(100000)

input = sys.stdin.readline
inf = float('inf')
 
n = int(input())
m = int(input())
dp = [inf] * (n + 1)
dp[0] = 0

for i in range(1, m + 1):
    x = int(input())
    for j in range(x, n + 1):
        dp[j] = min(dp[j], dp[j - x] + 1)

if dp[n] != inf:
    print("Roberta wins in", dp[n], "strokes.")
else:
    print("Roberta acknowledges defeat.")
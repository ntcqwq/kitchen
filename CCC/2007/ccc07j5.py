# CCC '07 J5 - Keep on Truckin'
# Concepts: 0-1 knapsack dp

from collections import deque
from bisect import bisect_left as bs
from itertools import permutations
import sys, math
import heapq as hq

# sys.setrecursionlimit(100000)

input = sys.stdin.readline
inf = float('inf')

A = int(input())
B = int(input())
N = int(input())

motel = [0, 990, 1010, 1970, 2030, 2940, 3060, 3930, 4060, 4970, 5030, 5990, 6010, 7000, inf] + [int(input()) for _ in range(N)]
motel.sort()

M = len(motel)

dp = [0] * M
dp[0] = 1

for i in range(0, M):
    dist = 0
    while motel[i+dist] - motel[i] <= B:
        if motel[i+dist] - motel[i] >= A:
            dp[i+dist] += dp[i]
        dist += 1
    
print(dp[-2])
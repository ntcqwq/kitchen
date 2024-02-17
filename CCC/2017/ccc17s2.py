from bisect import bisect_left, bisect_right
import sys

input = sys.stdin.readline

N = int(input())

tides = list(map(int, input().split()))
tides.sort()
bisected = int(N/2)
low = tides[0:bisect_left(tides, tides[bisected])+(1 if N % 2 == 1 else 0)]
high = tides[bisect_right(tides, tides[bisected-(1 if N % 2 == 0 else 0)]):N]
low.sort(reverse = True)
for i in range(len(low)):
    print(low[i], end = " ")
    try:
        print(high[i], end = " ")
    except IndexError:
        pass
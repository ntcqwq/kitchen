from collections import deque, defaultdict 
from bisect import bisect_left as bs
import sys, math, heapq as hq, itertools, copy
input, inf, mx, mod = sys.stdin.readline, 1e30, 302, 1000000007
# sys.setrecursionlimit(100000)

b1, b2 = 133, 10007

N = input().strip()
H = input().strip()
a, b = len(N), len(H)
psn = [0] * 26
psh = [0] * 26
for c in N:
    psn[ord(c)-ord('a')] += 1

hash1, hash2 = [0] * (b+1), [0] * (b+1)
pw1, pw2 = [1] * (b+1), [1] * (b+1)

for i in range(1, b+1):
    hash1[i] = (hash1[i-1]*b1+ord(H[i-1]))%mod
    hash2[i] = (hash2[i-1]*b2+ord(H[i-1]))%mod
    pw1[i] = pw1[i-1]*b1%mod
    pw2[i] = pw2[i-1]*b2%mod

ans = set()
for i in range(b):
    psh[ord(H[i])-ord('a')] += 1
    if i >= a: psh[ord(H[i-a])-ord('a')] -= 1
    if psn == psh:
        l, r = i-a+2, i+1
        ss1 = (hash1[r]-hash1[l-1]*pw1[r-l+1]+mod)%mod
        ss2 = (hash2[r]-hash2[l-1]*pw2[r-l+1]+mod)%mod
        ans.add((ss1, ss2))
print(len(ans))
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
freq = [0] * (N + 1)
a = []
L = R = distinct = ans = 0
while R < N:
    ai = int(input())
    a.append(ai)
    freq[ai] += 1
    if freq[ai] == 1:
        distinct += 1
    while distinct >= K:
        ans += N - R
        freq[a[L]] -= 1
        if freq[a[L]] == 0:
            distinct -= 1
        L += 1
    R += 1
print(ans)
import sys;
input = sys.stdin.readline;

N, M, K = map(int, input().split());

# N classes, class i ends at minute A(i) --> students walk through park, 1 minute leave
# Alice and Bob will stay in the park from 1 ... M minutes
# Bob he can make at most 1 class i up to K minutes earlier or later

optimal = 0;
A = [0, 0] + list(map(int, input().split())) + [M+1, M+1];
ds = []

for i in range(1, N+3):
    d = A[i] - A[i-1] - 1;
    ds.append(d)
    m = 0;
    m2 = 0;
    m = min(K, A[i-1] - A[i-2])
    m2 = min(K, A[i+1] - A[i])
    # print(d, m, m2)
    optimal = max(optimal, d + max(m, m2));
# print(A)
# print(ds)
print(optimal);
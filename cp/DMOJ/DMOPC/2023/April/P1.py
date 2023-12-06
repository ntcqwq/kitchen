import sys;
input = sys.stdin.readline;

N, M, K = map(int, input().split());

optimal = 0;
A = [0] + list(map(int, input().split())) + [M+1];

# print(A)
for i in range(N+1):
    d = A[i+1] - A[i] - 1;
    m = 0;
    m2 = 0;
    if A[i] < K-1: 
        if not i == 0:
            m = min(A[i], A[i] - A[i-1] - 1);
        else:
            m = A[i];
    elif A[i] >= K-1:
        if not i == 0:
            m = min(K, A[i] - A[i-1] - 1);
        else:
            m = K;
    if M - A[i+1] < K:
        if not i == N:
            m2 = min(M - A[i+1], A[i+2] - A[i+1]);
        else:
            m2 = M - A[i+1];
    elif M - A[i+1] >= K:
        if not i == N:
            m2 = min(K, A[i+2] - A[i+1]);
        else:
            m2 = K;
    optimal = max(optimal, d + max(m, m2));
print(optimal);
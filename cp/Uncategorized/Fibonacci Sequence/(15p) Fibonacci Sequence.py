# https://dmoj.ca/problem/fibonacci
# 100/100 Python 3

def multiply(A, B):
    C = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                C[i][j] = (C[i][j] + (A[i][k] * B[k][j]) % 1000000007) % 1000000007
    return C

def fibonacci(N):
    if N == 0:
        return 0
    elif N == 1:
        return 1
    else:
        M = [[1, 1], [1, 0]]
        result = [[1, 0], [0, 1]]
        N -= 1
        while N > 0:
            if N % 2 == 1:
                result = multiply(result, M)
            M = multiply(M, M)
            N = N // 2
        return result[0][0]

print(fibonacci(int(input())))
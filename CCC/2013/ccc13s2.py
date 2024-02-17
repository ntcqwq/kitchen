import sys;

input = sys.stdin.readline;

W = int(input());
N = int(input());
cw = [0] * N;
w = 0;

for i in range(N):
    cw[i] = int(input());
    w += cw[i];
    if (i >= 4):
        w -= cw[i-4];
    if (w > W):
        print(i);
        sys.exit();
print(N);

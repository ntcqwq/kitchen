import sys
input = sys.stdin.readline;

N, T = map(int, input().split());

cur = [bool(int(x)) for x in input().strip()];

b = 1;

while T > 0:
	if T % 2 != 0:
		n = [False] * N
		for i in range(N):
			if cur[i]:
				r = (((i + b) % N) + N) % N;
				l = (((i - b) % N) + N) % N;
				n[r] ^= True;
				n[l] ^= True;
		cur = n;
	T //= 2;
	b <<= 1;

print(''.join(str(int(x)) for x in cur));
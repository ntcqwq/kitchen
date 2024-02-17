import sys
input = sys.stdin.readline

def nH(mid):
	n = h
	length = mid * 2
	for i in range(h):
		if address[i] > (address[0] + length):
			break
		end = address[i]
		cnt = 1
		for j in range(i+1, h):
			if address[i] <= (address[j] + length) - 1000000:
				break
			if address[j] > end:
				end = address[j] + length
				cnt += 1
		n = min(n, cnt)
	return n

h = int(input())
address = [int(input()) for _ in range(h)]
address.sort()
k = int(input())

left, right = 0, 1000000

while (left < right):
	mid = left + (right-left)//2
	if nH(mid) <= k:
		right = mid
	else:
		left = mid+1

print(right)
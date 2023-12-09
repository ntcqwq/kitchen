import sys
input = sys.stdin.readline

goodl = [[1,0], [2,0], [3,0], [2,1]]
recl = [[1,1], [2,2], [3,1]]

T = int(input())

def rec(m, x, y):
	if m == 1:
		if [x, y] in goodl:
			return True
		else:
			return False
	size = 5 ** (m-1)
	x1 = x // size
	y1 = y // size
	if [x1, y1] in goodl:
		return True
	elif [x1, y1] in recl:
		return (rec(m-1, x % size, y % size))
	else:
		return False

for i in range(T):
	m, x, y = map(int, input().split())
	if rec(m, x, y):
		print('crystal')
	else:
		print('empty')
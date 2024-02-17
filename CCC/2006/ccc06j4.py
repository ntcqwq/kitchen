from queue import PriorityQueue
import sys

input = sys.stdin.readline

N = 7

indg = [-1, 1, 0, 0, 2, 1, 0, 1]
adjl =  [-1, [4, 7], [1], [4, 5], [], [], [], []]

q = PriorityQueue()

order = []

while True:
    a = int(input())
    b = int(input())
    if a == 0: 
        break
    adjl[a].append(b)
    indg[b] += 1

for i in range(1, N+1):
    if indg[i] == 0:
        q.put(i)

while not q.empty():
    y = q.get()
    order.append(y)
    for n in adjl[y]:
        indg[n] -= 1
        if indg[n] == 0:
            q.put(n)

if len(order) == N:
    print(*order)
else:
    print("Cannot complete these tasks. Going to bed.")

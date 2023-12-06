import sys
input = sys.stdin.readline

N = int(input())
pages = [[]]
for i in range(1, N + 1):
    pages.append([int(x) for x in input().split()][1:])
visited = [0] * (N + 1)
shortest = N + 1
counter = 0
q = [[1]]
visited[1] = 1
while q:
    counter += 1
    queued = q.pop()
    added = []
    for node in queued:
        for next in pages[node]:
            if not visited[next]:
                visited[next] = 1
                added.append(next)
        if not pages[node]:
            shortest = min(shortest, counter)
    if added:
        q.append(added)
print("Y" if sum(visited) == N else "N")
print(shortest)
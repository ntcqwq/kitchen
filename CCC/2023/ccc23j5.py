horizVertDir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
diagDir = [[1, 1], [-1, -1], [1, -1], [-1, 1]]
word = input()
n = int(input())
m = int(input())
grid = []
for i in range(n):
    grid.append(input().split((" ")))

visited = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(False)
    visited.append(row)

def isLegal(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

def dfs(x, y, characterNum, cur_dir, changed, dir, visited):
    count = 0
    if characterNum == len(word) - 1: #Found the whole word
        return 1
    visited[x][y] = True
    if characterNum == 0 or changed:
        newX = x + dir[cur_dir][0]
        newY = y + dir[cur_dir][1]
        if isLegal(newX, newY) and not visited[newX][newY] and grid[newX][newY] == word[characterNum + 1]:
            count += dfs(newX, newY, characterNum + 1, cur_dir, changed, dir, visited)
    else:
        for i in range(4):
            newX = x + dir[i][0]
            newY = y + dir[i][1]
            if isLegal(newX, newY) and not visited[newX][newY] and grid[newX][newY] == word[characterNum + 1]:
                count += dfs(newX, newY, characterNum + 1, i, cur_dir != i or changed, dir, visited)
    visited[x][y] = False
    return count


if len(word) <= 1:
    count = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == word[0]:
                count += 1
    print(count)
else:
    count = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == word[0]:
                for k in range(4):
                    count += dfs(i, j, 0, k, False, horizVertDir, visited)
                    count += dfs(i, j, 0, k, False, diagDir, visited)
    print(count)
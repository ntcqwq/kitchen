import sys
input = sys.stdin.readline
x = -1
y = -5
grid = {-1: [0], -2: [0], -3: [0, 1, 2, 3, 5, 6, 7], -4: [3, 5, 7], -5: [-1, 3, 4, 5, 7], -6: [-1, 7], -7: list(range(-1, 8))}
danger = False
while True:
    d, b = input().split()
    if d == "l":
        x1 = x
        x -= int(b)
        if not y in grid:
            grid[y] = list(range(min(x1,x),max(x,x1)))
        else:
            grid[y] += list(range(min(x1,x),max(x,x1)))
        if len(grid[y]) != len(set(grid[y])):
            danger = True
    elif d == "r":
        x1 = x
        x += int(b)
        if not y in grid:
            grid[y] = list(range(min(x1,x)+1,max(x,x1)+1))
        else:
            grid[y] += list(range(min(x1,x)+1,max(x,x1)+1))
        if len(grid[y]) != len(set(grid[y])):
            danger = True
    elif d == "u":
        y1 = y
        y += int(b)
        for i in range(min(y1,y)+1,max(y,y1)+1):
            if not i in grid:
                grid[i] = [x]
            else:
                grid[i].append(x)
            if len(grid[i]) != len(set(grid[i])):
                danger = True
    elif d == "d":
        y1 = y
        y -= int(b)
        for i in range(min(y1,y),max(y,y1)):
            if not i in grid:
                grid[i] = [x]
            else:
                grid[i].append(x)
            if len(grid[i]) != len(set(grid[i])):
                danger = True
    else:
        break
    print(x, y, end=" ")
    if danger:
        print("DANGER")
        break
    else:
        print("safe")
import sys
input = sys.stdin.readline
width = int(input())
height = int(input())
cwidth = int(input())
cheight = int(input())
N = int(input())
room = [[False for _ in range(width)] for _ in range(height)]


for row in range(height):
    for col in range(width):
        if row < cheight and col < cwidth:
            room[row][col] = True 
        if row < cheight and col >= width - cwidth:
            room[row][col] = True 
        if row >= height - cheight and col < cwidth:
            room[row][col] = True 
        if row >= height - cheight and col >= width - cwidth:
            room[row][col] = True 

R = 0
C = cwidth
D = 0



dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
room[R][C] = True
  
def getDirection(R, C, D):
    for i in range(3):
        d2 = (D + i + 3) % 4
        r2 = R + dirs[d2][0]
        c2 = C + dirs[d2][1]
        if r2 >= 0 and r2 < height and c2 >= 0 and c2 < width and room[r2][c2] == False:
            return d2
    else:
        return -1
    
for i in range(N):
    D = getDirection(R, C, D)
    if D >= 0: 
        R = R + dirs[D][0]
        C = C + dirs[D][1]
        room[R][C] = True
    else:
        break

print(C+1)
print(R+1)
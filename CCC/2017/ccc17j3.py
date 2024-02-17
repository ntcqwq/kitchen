# Read input values
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
c = int(input())

# Calculate the Manhattan distance
distance = abs(x2 - x1) + abs(y2 - y1)

# Check if it's impossible to reach the destination
if distance > c or (distance % 2 != c % 2):
    print("N")
else:
    print("Y")
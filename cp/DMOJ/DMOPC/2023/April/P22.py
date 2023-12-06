import sys
# read in canvas A
N, M = map(int, input().split())
A = []
for i in range(2):
    row = list(map(int, input().split()))
    A.append(row)

# read in canvas T
T = []
for i in range(2):
    row = list(map(int, input().split()))
    T.append(row)

# check if T can be created from A using Picasso's brushstroke
for k in range(-10, 11):
    # apply the brushstroke with k and horizontal flip
    A1 = [row[:] for row in A]
    A1[1][0] += k
    A1[1][1] += k
    A1 = [row[::-1] for row in A1]
    A1[1][0] += k
    A1[1][1] += k
    if A1 == T:
        print("YES")
        exit()
    # apply the brushstroke with k and vertical flip
    A2 = [row[:] for row in A]
    A2[1][0] += k
    A2[1][1] += k
    A2 = A2[::-1]
    A2[1][0] += k
    A2[1][1] += k
    if A2 == T:
        print("YES")
        sys.exit()

# if none of the brushstrokes match T, then T cannot be created from A
print("NO")

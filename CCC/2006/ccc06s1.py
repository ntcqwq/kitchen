import sys
input = sys.stdin.readline

dad = input().strip()
mom = input().strip()
# print(dad, mom)
possible = set()
letterIndex = 0
for i in range(0, 10):
    possibility = [dad[i], mom[letterIndex]]
    possibility2 = [dad[i], mom[letterIndex+1]]
    possible.add(sorted(possibility)[0])
    possible.add(sorted(possibility2)[0])
    if i % 2 == 1:
        letterIndex += 2
X = int(input())
for i in range(X):
    baby = input().strip()
    isBaby = True
    for j in baby:
        if j not in possible:
            isBaby = False
            break
    if isBaby:
        print("Possible baby.")
    else:
        print("Not their baby!")
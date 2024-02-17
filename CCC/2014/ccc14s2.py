import sys
N = int(input())
G1 = input().split()
G2 = input().split()

good = True
Class = {}
for student in range(N):
    s1 = G1[student]
    s2 = G2[student] 
    if s1 == s2:
        print("bad")
        sys.exit()
    if s2 in Class:
        ss1 = Class[s2]
        if ss1 in Class:
            if Class[ss1] != s2:
                print("bad")
                sys.exit()
    Class[s1] = s2
print("good")
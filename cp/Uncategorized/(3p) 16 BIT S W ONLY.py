import sys
input = sys.stdin.readline
N = int(input())
for _ in range(N):
    ns = input().split()
    if int(ns[0])*int(ns[1]) != int(ns[2]):
        print("16 BIT S/W ONLY")
    else:
        print("POSSIBLE DOUBLE SIGMA")
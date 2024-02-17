import sys
input = sys.stdin.readline
T = int(input())
nums = [float(input()) for _ in range(T)]
print('{:.4f}'.format(max(nums)))
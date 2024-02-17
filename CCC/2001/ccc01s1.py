from collections import deque
from bisect import bisect_left as bs
from itertools import permutations
import sys, math
import heapq as hq

# sys.setrecursionlimit(100000)

input = sys.stdin.readline
inf = float('inf')

s = input().strip()
suit = 0
cards = [[], [], [], []]
points = []
points_map = {'A' : 4, '2' : 0, '3' : 0, '4' : 0, '5' : 0, '6' : 0,
          '7' : 0, '8' : 0, '9' : 0, 'T' : 0, 'J' : 1, 'Q' : 2, 'K' : 3,
          'C' : 'C', 'D' : 'D', 'H' : 'H', 'S' : 'S'}

for i in range(17):
    if s[i] == 'C':
        suit = 0
    elif s[i] == 'D':
        suit = 1
    elif s[i] == 'H':
        suit = 2
    elif s[i] == 'S':
        suit = 3
    else:
        cards[suit].append(s[i])

for i in range(4):
    temp = list(map(points_map.get, cards[i]))
    points.append(sum(temp))

    if len(cards[i]) == 0:
        points[i] += 3
    elif len(cards[i]) == 1:
        points[i] += 2
    elif len(cards[i]) == 2:
        points[i] += 1

print('Cards Dealt              Points')
print('Clubs ' + ' '.join(cards[0]) + ' ' + str(points[0]))
print('Diamonds ' + ' '.join(cards[1]) + ' ' + str(points[1]))
print('Hearts ' + ' '.join(cards[2]) + ' ' + str(points[2]))
print('Spades ' + ' '.join(cards[3]) + ' ' + str(points[3]))
print('                       Total ' + str(sum(points)))
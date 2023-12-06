import sys
input = sys.stdin.readline

distance = int(input())
clubs = [int(input())]*(int(input()) + 1)
least = [5281]*(int(distance+1) + 1)
least[0] = 0

for i in range(distance+1):
  for j in range(len(clubs)):
    if i + clubs[j] <= distance:
      if least[i] + 1 < least[i+clubs[j]]:
        least[i+clubs[j]] = least[i] + 1
  
if least[distance] < 5281:
  print(f"Roberta wins in {str(least[distance])} strokes.")
else:
  print("Roberta acknowledges defeat.")
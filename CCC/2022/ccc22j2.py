players = int(input())
fs = 0
for player in range(players):
    points = int(input())
    fouls = int(input())
    if 5*points-3*fouls > 40:
        fs += 1

print(f'{fs}{"+" if fs == players else ""}')

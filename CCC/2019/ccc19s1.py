instructionLine = input()
start = [[1, 2],
         [3, 4]]

for instruction in instructionLine:
    if instruction == "H":
        start[0][0], start[1][0] = start[1][0], start[0][0]
        start[0][1], start[1][1] = start[1][1], start[0][1]
    else:
        start[0][0], start[0][1] = start[0][1], start[0][0]
        start[1][0], start[1][1] = start[1][1], start[1][0]

print(start[0][0], start[0][1])
print(start[1][0], start[1][1])

last = ""
while 1:
    instruction = input()
    if instruction == "99999":
        break
    direction = last if int(instruction[:2][0]) + int(instruction[:2][1]) == 0 else "right" if (int(instruction[:2][0]) + int(instruction[:2][1])) % 2 == 0 else "left"
    print(f'{direction} {instruction[-3:]}')
    last = direction
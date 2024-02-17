a = ["into your HOME."]

while True:
    action = input()
    if action == "R":
        a.append("Turn LEFT ")
    elif action == "L":
        a.append("Turn RIGHT ")
    elif action == "SCHOOL":
        break
    else:
        a.append(f"onto {action} street.")
a.reverse()

for x in zip(a[0::2], a[1::2]):
    print(''.join(x))


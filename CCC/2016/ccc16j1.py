all = int(bool()) 
for i in range(6):
    if input() == "W":
        all += 1
if all == 5 or all == 6:
    print(1)
elif all == 4 or all == 3:
    print(2)
elif all == 2 or all == 1:
    print(3)
else:
    print(-1)
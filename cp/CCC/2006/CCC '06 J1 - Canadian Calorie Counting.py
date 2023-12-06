food = [[461,431,420,0],[100,57,70,0],[130,160,118,0],[167,266,75,0]]
cals = 0
for i in range(4):
    order = int(input())
    cals += food[i][order-1]
print(f"Your total Calorie count is {cals}.")
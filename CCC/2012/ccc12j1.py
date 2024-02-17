l = int(input())
s = int(input())
if s <= l:
    print("Congratulations, you are within the speed limit!")
else:
    if s-l > 30:
        print("You are speeding and your fine is $500.")
    elif s-l > 20:
        print("You are speeding and your fine is $270.")
    else:
        print("You are speeding and your fine is $100.")
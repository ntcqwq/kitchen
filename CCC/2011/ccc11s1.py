text = ""
n = int(input())
for _ in range(n):
    text += input() + " "
text = text.lower()
if text.count("t") > text.count("s"):
    print("English")
else:
    print("French")
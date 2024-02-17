coldest = 256
coldestC = ""
while True:
    city = input().split()
    if int(city[1]) < coldest: 
        coldest = int(city[1])
        coldestC = city[0]
    if city[0] == "Waterloo": break
print(coldestC)
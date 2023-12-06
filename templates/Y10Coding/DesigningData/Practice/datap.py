import csv

with open("/Users/nchen26/Code/Journey/ntc/Sublime/countryInfo.csv", newline = '') as cd:
    reader = csv.reader(cd)
    countrydata = list(reader)[1:]

with open("/Users/nchen26/Code/Journey/ntc/Sublime/playerInfo.csv", newline = '') as pd:
    reader = csv.reader(pd)
    playerdata = list(reader)[1:]

countrydata.sort(key = lambda x: x[3])
regioncode = {}

for c in countrydata:
    regioncode[c[3].lower()] = {
        "name": c[2].split(",")[1] + " " + c[2].split(",")[0] if "," in c[2] else c[2],
        "total": 0,
        "players": 0
        }

for p in playerdata:
    if p[4] in regioncode:
        print(p[1], p[2], "is from", regioncode[p[4]]["name"].strip() + ". Earnings:", p[5] + "$")
        regioncode[p[4]]["total"] += float(p[5])
        regioncode[p[4]]["players"] += 1
    else:
        print(p[1], p[2], "is from", "Country not found" + ". Earnings:", p[5] + "$")

for c in regioncode:
    regioncode[c]["avg"] = regioncode[c]["total"] / (regioncode[c]["players"] if regioncode[c]["players"] != 0 else 1)
    print(regioncode[c]["avg"])
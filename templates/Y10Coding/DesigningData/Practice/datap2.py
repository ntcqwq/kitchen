import csv

def sortKeyC(k):
    return k[3]

def sortKeyP(k):
    return k[4]

with open("countryInfo.csv",newline='') as countryRawData:
    reader = csv.reader(countryRawData)
    countryData = list(reader)

with open("playerInfo.csv",newline='') as playerRawData:
    reader = csv.reader(playerRawData)
    playerData = list(reader)

countryData.pop(0)
playerData.pop(0)
countryData.sort(key = sortKeyC)
playerData.sort(key = sortKeyP)

playerInfo = []
i = 0
j = 0
while i < len(playerData):
    code = playerData[i][4]

    while j < len(countryData) and code.lower() != countryData[j][3].lower():
        j += 1
    if j < len(countryData):
        playerInfo.append([playerData[i][1], playerData[i][2], countryData[j][2], playerData[i][5]])
    else:
        playerInfo.append([playerData[i][1], playerData[i][2], code, playerData[i][5]])
        j = 0 
    i += 1

countryavgs = []
i = 0
while i < len(playerInfo):
    count = 0
    sum = 0
    country = playerInfo[i][2]
    while i < len(playerInfo) and country == playerInfo[i][2]:
        sum += float(playerInfo[i][3])
        count += 1
        i += 1
    average = sum / count
    countryavgs.append([average, country, count])

countryavgs.sort()

for i in countryavgs:
    average, country, count = i
    print(country, average, count)

# from pylab import *; set_loglevel('debug'); plot(); show()
# "

# import csv

# with open('data.csv') as file:
#     csv_reader = tuple(csv.reader(file, delimiter=','))
#     data = {}
#     for place in csv_reader:
#         if not place[0] in data:
#             data[place[0]] = {
#                 "code": place[1],
#                 place[2]: place[3]
#             }
#         else:
#             data[place[0]][place[2]] = place[3]

#     print(f'Number of total countries/regions: {len(data)}')
#     for item in data:
#         print(item, f"({data[item]['code'] if not data[item]['code'] == '' else 'Region'})")
#         for year in data[item]:
#             if year != "code":
#                 print(f'{year}: {data[item][year]}')
#         print()

# import csv

# with open("data.csv") as rawData:
#     reader = csv.reader(rawData)
#     dataIn = list(reader)

# i = 1
# countryData = []
# while i < len(dataIn) :
#     if dataIn[i][1] != "" and dataIn[i][0] != "World" and int(dataIn[i][2]) >= 2000:
#         countryData.append(dataIn[i])
#     i += 1

# for country in countryData:
#     print(country)
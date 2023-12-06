import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import csv

def loadList(fileName):
    with open(fileName, newline='') as f:
        reader = csv.reader(f)
        dataList = list(reader)
    return dataList

barEnergy = loadList("RenewableEnergyCapacity.csv")

i = 1
provinceData = []
while i < len(barEnergy):
    if barEnergy[i][0] not in ["Canada", '']:
        provinceData.append(barEnergy[i][0:4])
    i += 1

data = {}
for p in provinceData:
    province, energy, year, d = p
    year, d = int(year), float(d)
    if not energy in data:
        data[energy] = {}
    if not year in data[energy]:
        data[energy][year] = [0, 0]
    data[energy][year][0] += d
    data[energy][year][1] += 1

width = 0.1

y = [[] for _ in range(8)]
legend = ["Hydro", "Wind", "Biomass", "Solar", "Nuclear", "Coal", "Natural Gas", "Oil and Diesel"]
x = np.arange(2004, 2016) 

for e in data:
    for yr in data[e]:
        y[legend.index(e)].append(data[e][yr][0]/(data[e][yr][1] if data[e][yr][1] != 0 else 1))


plt.bar(x-0.4, y[0], width, color='red')
plt.bar(x-0.3, y[1], width, color='orange')
plt.bar(x-0.2, y[2], width, color='yellow')
plt.bar(x-0.1, y[3], width, color='green')
plt.bar(x, y[4], width, color='cyan')
plt.bar(x+0.1, y[5], width, color='blue')
plt.bar(x+0.2, y[6], width, color='purple')
plt.bar(x+0.3, y[7], width, color='pink')

plt.legend(legend) 
plt.show() 


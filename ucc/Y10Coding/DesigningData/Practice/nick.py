import csv
import matplotlib.pyplot as plt
import pandas as pd
import mplcursors


# What we want to happen when hovering over a point 'event'.
def handle_hover_event(sel):
    countryinfo = sel.target.index
    info = Country[countryinfo]
    text = f"{info}\nTransport Emissions: {TransportEmissions[countryinfo]}\nTotal Emissions: {TotalEmissions[countryinfo]}"
    sel.annotation.set_text(text)


with open("gonnatrythisagain.csv", newline='') as EmissionsData:
    reader = csv.reader(EmissionsData)
    Emissions = list(reader)

EmissionsInfo = []
i = 1
colors = []

while i < len(Emissions):
    if Emissions[i][0] != "Canada" and Emissions[i][0] != "United States":
        EmissionsInfo.append([Emissions[i][0], Emissions[i][11], Emissions[i][12]])
        colors.append('black')
    i+= 1

Country = [entry[0] for entry in EmissionsInfo]
TotalEmissions = [float(entry[1]) for entry in EmissionsInfo]
TransportEmissions = [float(entry[2]) for entry in EmissionsInfo]

fig, ax = plt.subplots()

j = 1
while j < len(Emissions):
    if Emissions[j][0] == "Canada" or Emissions[j][0] == "United States":
        EmissionsInfo.append([Emissions[j][0], Emissions[j][11], Emissions[j][12]])
        colors.append('red')
    j+= 1

Country = [entry[0] for entry in EmissionsInfo]
TotalEmissions = [float(entry[1]) for entry in EmissionsInfo]
TransportEmissions = [float(entry[2]) for entry in EmissionsInfo]

plt.scatter(TransportEmissions, TotalEmissions, color=colors)

ax.set_ylabel("Total CO2 Emissions Proportional to Population")
ax.set_xlabel("Transport C02 Emissions Proportional to Population")
ax.set_title('Fueling the Climate Crisis - Canada and USAs Astounding Transport Emissions Are Huge Outliers')

factor = 0 
nTicks = [0]
tickLabels1 = ['0']
tickLabels2 = ["0"]
while factor < 10:
    factor += 1
    nTicks.append(factor)
    tickLabels1.append(str(factor))
    tickLabels2.append(str(factor))

ax.set_yticks(nTicks, labels=tickLabels1)
ax.set_xticks(nTicks, labels=tickLabels2)

# Turn on hover annotations

mplcursors.cursor(hover=True).connect("add", handle_hover_event)

plt.show()
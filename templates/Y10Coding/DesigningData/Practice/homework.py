import matplotlib.pyplot as plt
import pandas as pd
import csv, random

#Making multiple plots
 
#Each plot can be of different data, or you can reuse data in a different way.
#Note that dataSet3 is plotted twice

with open('coviddata.csv') as file:
    # reading the file coviddata.csv
    covid_reader = list(csv.reader(file))[1:]

# to make data easier to read, sorting people by their "id". This "id" is a unique key that we can use
covid_reader.sort(key = lambda x: int(x[0]))

# we are going to store all data analysed in a dictionary
data = {}
data3 = [[0, 0] for _ in range(20)]

for person in covid_reader:
    # remove bad data
    person.pop(65)
    person.pop(4)
    person.pop(-1)

    # convert [String] to [Int]
    person = list(map(int, person))

    # extract useful data
    pid, gender, age, primary_electronic_devices, device_use_frequency_covid, device_use_frequency_before, duration_per_day_covid, duration_per_day_before, degree_of_addiction_covid, degree_of_addiction_before, IAT_total, anxiety_classification_3, depression_classification_3, stress_classification_3 = person[0], person[2], person[3], person[10], person[11], person[12], person[13], person[14], person[19], person[20], person[63], person[68], person[69], person[70]

    # append them in a dictionary 
    data[pid] = {
        'gender': 'blue' if gender == 1 else 'red',
        'age': age,
        'devices': primary_electronic_devices,
        'use_freq': device_use_frequency_covid,
        'use_increase': device_use_frequency_covid - device_use_frequency_before,
        'duration_avg': duration_per_day_covid,
        'duration_increase': duration_per_day_covid - duration_per_day_before
    }
    data3[age][0] += duration_per_day_covid
    data3[age][1] += 1

# the 5 "variables" that determine xpos, ypos, size, color, and transparency 
dataSet1 = []
dataSet2 = []
dataSet3 = []
dataSet4 = []

for i in data:
    # for each data point, append them into corresponding axis, also add a bit of randomness cus why not
    dataSet1.append([data[i]['age'] + random.choice([-0.5, -0.4, -0.3, -0.2, -0.1, 0, 0.1, 0.2, 0.3, 0.4]), data[i]['duration_avg'] + random.choice([-0.5, -0.4, -0.3, -0.2, -0.1, 0, 0.1, 0.2, 0.3, 0.4])])
    dataSet2.append([data[i]['use_increase'], data[i]['duration_increase']])
    dataSet3.append([data[i]['age']+ random.choice([-0.5, -0.4, -0.3, -0.2, -0.1, 0, 0.1, 0.2, 0.3, 0.4]), data[i]['use_freq'] + random.choice([-0.5, -0.4, -0.3, -0.2, -0.1, 0, 0.1, 0.2, 0.3, 0.4])])

for i in range(18):
    dataSet4.append([i, int(data3[i][0]/(data3[i][1] if data3[i][1] != 0 else 1))])

df1 = pd.DataFrame(dataSet1, columns=["Code", "Val"])
df2 = pd.DataFrame(dataSet2, columns=["Code", "Val"])
df3 = pd.DataFrame(dataSet3, columns=["Code", "Val"])
df4 = pd.DataFrame(dataSet4, columns=["Code", "Val"])

print(data3)

#This line establishes the number of plots you want to make
#fig is the whole plot, ax is a table where each cell is one of the plots
#experiment with different numbers in the figsize() arguement
#what would have to change if you wanted all 4 plots side by size?
fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(10,10))

#now each plot is simply an individual item in the list - treated as you would any other plot
ax[0, 0].scatter(df3.Code, df3.Val, color="red")
ax[0, 1].barh(df2.Code, df2.Val, color = "green")
ax[1, 0].plot(df4.Code, df4.Val, color = "black")
ax[1, 1].scatter(df1.Code, df1.Val, color="orange")

###############################################################
#make the numeric axis scale the same for all 4 plots
#ax[0,0].set_ylim([0,20])
###############################################################
#But this does not work because of the horizontal bar chart
#so instead use the code below
###############################################################
#note the difference for the horizontal bar
# ax[0,1].set_xlim([0,20])
# ax[1,0].set_ylim([0,20])
# ax[1,1].set_ylim([0,20])
################################################################

#set titles for each of the charts
################################################################
# ax[0, 0].set_title('0,0 is upper left')
# ax[0, 1].set_title('0,1 is top right')
# ax[1, 0].set_title("1,0 is bottom left")
# ax[1, 1].set_title('1,1 is bottom right')
################################################################
#But because the charts are so close together, this doesn't look good
################################################################
#this will fix the spacing
#fig.tight_layout()
################################################################
#Try setting the x and y axis titles for the charts (just make something up)
################################################################
 
################################################################
#the default numeric axis is by 5s
#change it to count by twos
#you can also add additional characters if you want
factor = 2
nTicks = [0]
tickLabels = ["0!"]
while factor <= 20:
    nTicks.append(factor)
    factor +=2
    tickLabels.append(str(factor) + "!")
#################################################################
#the lists created in the code above are used here:
################################################################
#if all of your plots have the same x and y axes you can set all of the ticks together
#plt.setp(ax, yticks=nTicks)
################################################################
#but in this case it doesn't work for the horizontal bar chart
#so you can set them individually
#note how the first chart's ticks are a little different
#ax[0,0].set_yticks(nTicks, labels=tickLabels)
# ax[0,1].set_xticks(nTicks)
# ax[1,0].set_yticks(nTicks)
# ax[1,1].set_yticks(nTicks)
################################################################

plt.show()
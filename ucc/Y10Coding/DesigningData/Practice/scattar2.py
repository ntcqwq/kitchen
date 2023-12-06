from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import random
import csv

with open('coviddata.csv') as file:
    # reading the file coviddata.csv
    covid_reader = list(csv.reader(file))[1:]

# to make data easier to read, sorting people by their "id". This "id" is a unique key that we can use
covid_reader.sort(key=lambda x: int(x[0]))

# we are going to store all data analysed in a dictionary
data = {}

for person in covid_reader:
    # remove bad data
    person.pop(65)
    person.pop(4)
    person.pop(-1)

    # convert [String] to [Int]
    person = list(map(int, person))

    # extract useful data
    pid, gender, age, primary_electronic_devices, device_use_frequency_covid, device_use_frequency_before, duration_per_day_covid, duration_per_day_before, degree_of_addiction_covid, degree_of_addiction_before, IAT_total, anxiety_classification_3, depression_classification_3, stress_classification_3 = person[
        0], person[2], person[3], person[10], person[11], person[12], person[13], person[14], person[19], person[20], person[63], person[68], person[69], person[70]

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

# the 5 "variables" that determine xpos, ypos, size, color, and transparency
x, y, z, c, a = [], [], [], [], []

for i in data:
    # for each data point, append them into corresponding axis, also add a bit of randomness cus why not
    x.append(data[i]['age'] + random.choice([-0.5, -0.4, -0.3, -0.2, -0.1, 0, 0.1, 0.2, 0.3, 0.4]))
    y.append(data[i]['duration_avg'] + random.choice([-0.5, -0.4, -0.3, -0.2, -0.1, 0, 0.1, 0.2, 0.3, 0.4]))
    z.append(data[i]['use_freq'] * 150)
    c.append(data[i]['gender'])
    a.append(data[i]['devices'] / 15)

# Creating figure
fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111)

# plot axis
scatter = ax.scatter(x, y, s=z, c=c, alpha=a, marker='o', label='Data')

plt.title("Age vs Average Duration on electronic devices during COVID")
plt.xlabel("Age (Years)")
plt.ylabel("Duration (Hours)")

# add legend
legend = ax.legend()
legend.legendHandles[0]._sizes = [30]  # adjust legend marker size

# show plot
plt.show()

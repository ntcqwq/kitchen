import csv
import matplotlib.pyplot as plt

# Data from the provided information
data1 = [
    ["0-9", 1.9],
    ["10-19", 4.7],
    ["20-29", 9.6],
    ["30-39", 11.9],
    ["40-49", 13.1],
    ["50-59", 14.3],
    ["60-69", 15.0],
    ["70-79", 13.8]
]

data2 = [
    ["0-9", 1.2],
    ["10-19", 3.8],
    ["20-29", 8.2],
    ["30-39", 9.9],
    ["40-49", 11.5],
    ["50-59", 13.7],
    ["60-69", 14.4],
    ["70-79", 13.0]
]

# Creating a CSV file to store the combined data
csv_file_path = "combinedEmissions.csv"
with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Age Group", "Shanghai and Tokyo 2022", "Shanghai and Tokyo 1985"])
    writer.writerows(zip([row[0] for row in data1], [row[1] for row in data1], [row[1] for row in data2]))

# Reading data from the CSV file
with open(csv_file_path, newline='') as emissionsRawData:
    reader = csv.reader(emissionsRawData)
    header = next(reader)  # Skip the header row
    combined_data = list(reader)

# Extracting data for the grouped bar chart
age_groups = [row[0] for row in combined_data]
emissions_2022 = [float(row[1]) for row in combined_data]
emissions_1985 = [float(row[2]) for row in combined_data]

# Creating a color dictionary for each dataset
colors = {'Shanghai and Tokyo 2022': 'forestgreen', 'Shanghai and Tokyo 1985': 'limegreen'}

# Creating a grouped bar chart with specified colors
bar_width = 0.35
fig, ax = plt.subplots()
bar1 = ax.bar(age_groups, emissions_2022, bar_width, label='Shanghai and Tokyo 2022', color=colors['Shanghai and Tokyo 2022'])
bar2 = ax.bar([index + bar_width for index in range(len(age_groups))], emissions_1985, bar_width, label='Shanghai and Tokyo 1985', color=colors['Shanghai and Tokyo 1985'])

ax.set_xlabel('Age Group (years)')
ax.set_ylabel('Average CO2 Emissions Per Person Per Year (metric tons)')
ax.set_title('Average CO2 Emissions by Age Group in Shanghai and Tokyo (2022 and 1985)')
ax.legend()

plt.show()
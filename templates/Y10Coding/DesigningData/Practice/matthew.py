import csv
import matplotlib.pyplot as plt

def read_file(file_path: str, remove_first_line = True) -> list:
    with open(f"{file_path}.csv", newline = '') as cd:
        reader = csv.reader(cd)
        return list(reader)[1:] if remove_first_line else list(reader)

# This function reads the csv file 'mental'
mental_data = read_file('mental')
# we use a pair array list to store the total depression score foro each age. data[0] is 18, data[1] is 19... so on.
data = [[] for age in range(18, 24+1)]
totalPeople = [0] * 9
for i in mental_data:
    age, depression, anxiety, panic, seekhelp = i[2], i[-4], i[-3], i[-2], i[-1]
    if age != '':
        age = int(age)
        data[age-18] += [depression, anxiety, panic, seekhelp]
        totalPeople[age-18] += 1 

organized_data = {}
for i in range(len(data)):
    organized_data[i+18] = data[i].count('Yes')/ totalPeople[i] if totalPeople[i] != 0 else 1

colors = ['#2C3E50', '#3498DB', '#E74C3C', '#2ECC71', '#9B59B6', '#F39C12', '#1ABC9C', '#D35400']

courses = list(organized_data.keys())
values = list(organized_data.values())
  
fig = plt.figure(figsize = (10, 9))
 

plt.bar(courses, values, color =colors, width = 0.4) 
plt.xlabel("<Whatever x label you want to put here>")
plt.ylabel("<Whatever y label you want to put here>")
plt.title("<Whatever title name you want to put here>")

plt.show()
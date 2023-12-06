import csv

def readfile(file_path):
    with open(file_path) as file:
        # reading the file
        reader = list(csv.reader(file))[1:]
        return reader

# to make data easier to read, sorting people by their "id". This "id" is a unique key that we can use
covid_reader = readfile('coviddata.csv')
diablo_reader = readfile('socialdiablo.csv')
university_reader = readfile('universitystudents.csv')

idsort = lambda x: int(x[0])
covid_reader.sort(key=idsort)
diablo_reader.sort(key=idsort)
university_reader.sort(key=idsort)

# store all data in an array
data = [[[0, 0] for _ in range(9)] for _ in range(30)]

for person in covid_reader:
    # remove bad data
    person.pop(65)
    person.pop(4)
    person.pop(-1)
    # convert [String] to [Int]
    person = list(map(int, person))
    # Number,totalseconds,Gender,Age,Birthday,Residence,The_only_child,Education_status,Mother_Education_Level,Father_Education_Level,Income_per_year,the_primary_electronic_devices,Frequency_COIVD2019,Frequency_before,Duration_per_day_COIVD2019,Duration_per_day_before,Frequency_of_use_after_0000_COIVD2019,Frequency_of_use_after_0000_before,Frequency_of_overnight_COIVD2019,Frequency_of_overnight_before,Degree_of_addiction_COVID2019,Degree_of_addiction_before,IAT1,IAT2,IAT3,IAT4,IAT5,IAT6,IAT7,IAT8,IAT9,IAT10,IAT11,IAT12,IAT13,IAT14,IAT15,IAT16,IAT17,IAT18,IAT19,IAT20,DASS1,DASS2,DASS3,DASS4,DASS5,DASS6,DASS7,DASS8,DASS9,DASS10,DASS11,DASS12,DASS13,DASS14,DASS15,DASS16,DASS17,DASS18,DASS19,DASS20,DASS21,totalvalue,IAT_total,IAT_classification,DASS_anxiety,DASS_depression,DASS_Stress,IAT_classification_3,Anxiety_classification_3,Depression_classification_3,Stress_classification_3,IAT40��
    pid, gender, age, primary_electronic_devices, device_use_frequency_covid, device_use_frequency_before, duration_per_day_covid, duration_per_day_before, degree_of_addiction_covid, degree_of_addiction_before, IAT_total, anxiety_classification_3, depression_classification_3, stress_classification_3 = person[0], person[2], person[3], person[10], person[11], person[12], person[13], person[14], person[19], person[20], person[63], person[68], person[69], person[70]
    # append the duration and count onto the data in order to solve for average later.
    data[age][7][0] += duration_per_day_covid
    data[age][7][1] += 1
    data[age][9][0] += device_use_frequency_covid
    data[age][9][1] += 1
    data[age][3][0] += primary_electronic_devices
    data[age][3][1] += 1
    

for person in diablo_reader:
    age, mentalhealth, devices = person
# with open("Day-25 CSV Files and Analysing Data with Pandas/weather_data.csv") as weather_data:
#     data = weather_data.readlines()
#     print(data[0].strip())

import csv

with open("Day-25 CSV Files and Analysing Data with Pandas/weather_data.csv") as weather_data:
    data = csv.reader(weather_data)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)
import pandas

data = pandas.read_csv("weather_data.csv")
print(type(data)) # tüm tablonun olduğu veri tipini pandas DataFrame olarak işliyor
print(type(data["temp"])) # Tablo içerisinde bir sütundaki verileri de liste şeklinde Series olarak 

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

average = sum(temp_list) / len(temp_list)
print(average)

print(data["temp"].max())

# Get data in columns
print(data["condition"])
print(data.condition)

# Get Data in Row
print(data[data.day == "Monday"])

# Get highest temp data
print(data[data.temp == data["temp"].max()])

# Create a dataframe from scratch
data_dict = {
    "students": ["Burak", "Armağan", "Biz"],
    "scores": [50,100,100]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
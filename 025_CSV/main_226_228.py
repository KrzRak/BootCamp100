###-----------------------------------------###
# 227.Printing data from csv file
#
# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

###-----------------------------------------###
# 227.Moving one colum to another table and printing them as an int
#
# import csv 
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

###-----------------------------------------###
# 227.Using pandas for csv

# import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data)
# print(data["temp"])

###-----------------------------------------###
# 228. DataFrames and Series
# import pandas

# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)

###-----------------------------------------###
# 228. Challenge 
import pandas

def Avg(list):
    return sum(list) / len(list)

data = pandas.read_csv("weather_data.csv")
temp_list = data["temp"].to_list()

average = Avg(temp_list)
print(average)

print(data["temp"].mean())

print(data["temp"].max())

###-----------------------------------------###
# Get data from columns
# print(data["condition"])
# print(data.condition)


###-----------------------------------------###
# Get data from row
print(data[data.day == "Monday"])

# Highest temperature
idmax = data.temp.idxmax()
print(data[data.index == idmax])
# Better -> output multiple rows
print(data[data.temp == data.temp.max()])

# Temp from Monday in F
monday = data[data.day == "Monday"]
monday_in_F = int(monday.temp) * 1.8 + 32
print(monday_in_F)


# Create a dataframe from a scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")
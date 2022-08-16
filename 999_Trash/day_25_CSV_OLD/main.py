# with open("weather_data.csv", mode="r") as weather_data:
#     data = weather_data.readlines()
# print(data)
# --------------------------------------------------------------------
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
# --------------------------------------------------------------------

# import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data)
# print(data["temp"])
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
# # sum_temp = 0
# # for temp in temp_list:
# #     sum_temp += temp
# # average_temp = sum_temp / len(temp_list)
# # print(round(average_temp, 1))
#
# print(data["temp"].mean())
# print(data["temp"].max())
#
# # Get data in Columns
# print(data["temp"])
# print(data.temp)

# # Get data in Row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# # Monday temp C -> F
# print(int(monday.temp) * 1.8 + 32)

# # Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

import pandas

# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray = "Gray"
cinnamon = "Cinnamon"
black = "Black"

gray_nr = 0
cinnamon_nr = 0
black_nr = 0

# for color in data["Primary Fur Color"]:
#     if color == gray:
#         gray_nr += 1
#     elif color == cinnamon:
#         cinnamon_nr += 1
#     elif color == black:
#         black_nr += 1
#
# color_data = {
#     "Fur Color": [gray, cinnamon, black],
#     "Squirrel Amount": [gray_nr, cinnamon_nr, black_nr]
# }
#
# color_data_csv = pandas.DataFrame(color_data)
# color_data_csv.to_csv("Color_count.csv")


data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

color_data = {
    "Fur Color": [gray, cinnamon, black],
    "Squirrel Amount": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

color_data_csv = pandas.DataFrame(color_data)
color_data_csv.to_csv("Color_count_faster_way.csv")
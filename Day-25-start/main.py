# # with open("weather_data.csv") as data_file:
# #     data = data_file.readlines()
#
# #or without /
# # import csv
# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temperatures = []
# #     for row in data:
# #         if row[1] != "temp":
# #             temperatures.append(row[1])
# #     print(temperatures)
#
#
# # or using pandas
import pandas
# from numpy.ma.core import maximum
#
# data = pandas.read_csv("weather_data.csv")
# print(data["temp"])
#
# # to dictionary
# data_dict = data.to_dict()
# print(data_dict)
#
# # to list
# data_temp = data["temp"].to_list()
# print(data_temp)
#
# # calculate average
# average = sum(data_temp)/ len(data_temp)
# print(average)
# #or
# print(data["temp"].mean())
#
# #max
# print(data["temp"].max())
#
#
# #Get data in columns
# print(data["condition"])
# #or
# print(data.condition)

#Get data in rows
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)
# #convert to fahrenheit
# monday_temp =monday.temp
# monday_temp_f =(monday_temp * 9/5 + 32)
# print(monday_temp_f)

#create a dataframe from scratch
data_dict = {
    "students": ["Amy","James","Angela"],
    "scores": [76,56,65]
}
data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")
# with open("weather_data.csv", mode='r') as weather:
#     mylist = weather.readlines()
# print(mylist)


# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     list = []
#     next(data)
#     for row in data:
#         list.append(int(row[1]))
#
#     print(list)


import pandas
data = pandas.read_csv("weather_data.csv")

# #
# # print(type(data))
# # print(data["temp"])
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()

# avg = 0
# #
# # for x in temp_list:
# #     avg += x
# #
# # print(avg/len(temp_list))
#
# print(sum(temp_list)/len(temp_list))

#print(data.condition)

#print(data["temp"].mean())
#print(data["temp"].max())


# print(data[data.temp == data["temp"].max()])
#
# monday = data[data.day == "Monday"]
# print(monday.condition)
#

# for x in data.temp:
#     x += 32
#     print(x)
#
# temp_1 = int(data[data.day == "Monday"].temp)
# print(temp_1 + 32)


data_dict = {
    "Students": ["Edson", "Vanessa", "Benito"],
    "Scores": [10, 20, 30]
}
data_dicts = pandas.DataFrame(data_dict)
print(data_dicts)
data_dicts.to_csv("new_data.csv")
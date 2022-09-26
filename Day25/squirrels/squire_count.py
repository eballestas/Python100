import pandas


data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")


grey_squirels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirels_count = len(data[data["Primary Fur Color"] == "Black"])


data_dict = {
    "Fur Color": ["Grey", "Cinnamon", "Black"],
    "Count": [grey_squirels_count, red_squirels_count, black_squirels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirles_count.csv")

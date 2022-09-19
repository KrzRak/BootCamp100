# Return amount of squirel color in another csv
import pandas

squirrel = pandas.read_csv("/home/dzyniu/VSCode/Phyton/BootCamp100/025_CSV/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# Count each colour
g_amount = squirrel["Primary Fur Color"].value_counts().Gray
c_amount = squirrel["Primary Fur Color"].value_counts().Cinnamon
b_amount = squirrel["Primary Fur Color"].value_counts().Black

# Create csv for color count
count_dict = {
    "Colour": ["Gray", "Cinnamon", "Black"],
    "Amount": [g_amount, c_amount, b_amount]
}
color_count = pandas.DataFrame(count_dict)
color_count.to_csv("Colour_count.csv")
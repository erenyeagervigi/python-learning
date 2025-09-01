import  pandas as pd

# data = pd.read_csv("weather_data.csv")
# # datas = data['temp'].to_list()
# #
# # # day_high = data[data.temp == data.temp.max()]
# # # print(f"hottest day {day_high.day}")
# # # print(f"condition {day_high.condition}")
# # print(datas)
#
# monday = data[data.day == "Monday"]
# print(f"temperature in fahrenheit: {monday.temp[0] * 9/5 + 32}")
# print(f"temperature in fahrenheit: {monday.temp * 9/5 + 32}")
#
# data_dict = {
#     "students" : ["eren", "mikasa", "armin"],
#     "marks": [7,8,10]
# }
# smth = pd.DataFrame(data_dict)
# smth.to_csv("aot_marks.csv")
#
# print(smth[smth.marks == smth.marks.max()].to_string(index = False))
# print(f"{smth.marks.mean():.1f}")

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250417.csv")
color = data["Primary Fur Color"].value_counts()
# gray_color = 0
# cinnamon = 0
# black = 0
#
# for col in color:
#     if col == "Gray":
#         gray_color += 1
#     if col == "Black":
#         black += 1
#     if col == "Cinnamon":
#         cinnamon += 1
#
colour = {
    "Fur": ["Gray", "Cinnamon", "Black"],
    "color_count": [
        color.get("Gray"),
        color.get("Cinnamon"),
        color.get("Black")
    ]
}

colour_data = pd.DataFrame(colour)
colour_data.to_csv("colour_data1.csv", index= False)


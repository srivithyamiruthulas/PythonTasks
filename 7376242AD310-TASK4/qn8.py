weather_data = [[22, 24, 21, 25, 23, 26, 22],
                [28, 29, 30, 31, 28, 27, 29], 
                [20, 22, 19, 21, 20, 22, 21]]

averages = [sum(week) / len(week) for week in weather_data]
hottest = max(temp for week in weather_data for temp in week)
hot_week = averages.index(max(averages)) + 1

print("Weekly Averages:", averages)
print("Hottest Temp:", hottest)
print("Hottest Week:", hot_week)

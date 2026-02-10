pollution = {"CityA": [50, 60, 70], "CityB": [120, 150, 130]}

avg_aqi = {city: sum(val)/len(val) for city, val in pollution.items()}
worst_city = max(avg_aqi, key=avg_aqi.get)

print(avg_aqi)
print(worst_city)

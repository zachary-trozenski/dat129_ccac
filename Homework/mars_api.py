import json
import requests
import statistics

"""
This program will query the MAAS2 API to pull information transmitted from the Mars
Curiosity Rover. Specifically I'd like to understand the average high and low
temperatures for the past 30 days, the maximum and mininum in the range of 30 sols,
 and the mode of the atmospheric opacity.
"""

mars_url = "https://api.maas2.apollorion.com"

max_temp = []
min_temp = []
atmospheric_opacity = []

def parse_martian_json_data():
    for sol in range(2548,2668):
        data = requests.get(mars_url + "/" + str(sol) + "/")
        json_obj = json.loads(data.text)
        
        max_temp.append(json_obj['max_temp'])
        min_temp.append(json_obj['min_temp'])
        atmospheric_opacity.append(json_obj['atmo_opacity'])


    temp_max_mean = statistics.mean(max_temp)
    max_max_temp = max(max_temp)
    temp_min_mean = statistics.mean(min_temp)
    min_min_temp = min(min_temp)
    atmo_mode = statistics.mode(atmospheric_opacity)

# Maybe let's try the final 120 days just for kicks
    print("Over the final 60 sols worth of weather data recorded by the Curiosity rover" +
        " we can determine the following statistics.")
    print("The average high temperature:", temp_max_mean, "Celsius.")
    print("The average low temperature:", temp_min_mean, "Celsius.")
    print("Atmospheric extremes reached lows of", min_min_temp, "Celsius and highs of", max_max_temp, "Celsius.")
    print("For what it's worth, most of the days it was", atmo_mode, ".")


def main():
    parse_martian_json_data()

if __name__ == "__main__":
    main()  

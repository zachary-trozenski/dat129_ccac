import json
import requests
import statistics

"""
This program will query the MAAS2 API to pull information transmitted from the Mars
Curiosity Rover. Specifically I'd like to understand the average high and low
temperatures for the past 30 days, the maximum and mininum in the range of 60 sols,
 and the mode of the atmospheric opacity.
"""

# Initialize the api URL as a variable
mars_url = "https://api.maas2.apollorion.com"

# Initialize the lists to store the values pulled from the json received from API
max_temp = []
min_temp = []
atmospheric_opacity = []

def parse_martian_json_data():
    """
    This is the main sequence of the program. A for loop is established based on
    the number of sols to be queried. In this case it's 60 sols. The API URL 
    is iterated over in the for loop sending the particular sol number to the end
    of the URL. For each sol in the range, the data is retrieved one by one
    and stored temporarily in a variable. That variable is then parsed for specific keys
    (temperatures and atmospheric opacity) and each value from the key is added to the 
    lists initialized above. This repeats for each sol in the range.
    """
    for sol in range(2608,2668):
        data = requests.get(mars_url + "/" + str(sol) + "/")
        json_obj = json.loads(data.text)
        
        max_temp.append(json_obj['max_temp'])
        min_temp.append(json_obj['min_temp'])
        atmospheric_opacity.append(json_obj['atmo_opacity'])

# Calculate the statistics (mean, min, max) for temperture and mode for atmospheric opacity
    temp_max_mean = statistics.mean(max_temp)
    max_max_temp = max(max_temp)
    temp_min_mean = statistics.mean(min_temp)
    min_min_temp = min(min_temp)
    atmo_mode = statistics.mode(atmospheric_opacity)

    print()
    print("Over the final 60 sols worth of weather data recorded by the Curiosity rover" +
        " we can determine the following statistics about the temperature and" +
        " and atmospheric conditions on Mars.")
    print("")
    print("The average high temperature: {:4,.1f} degrees Celsius.".format(temp_max_mean))
    print("The average low temperature: {:4,.1f} degrees Celsius.".format(temp_min_mean))
    print("Atmospheric extremes reached lows of", min_min_temp, " degrees Celsius and highs of", max_max_temp, "degrees Celsius.")
    print()
    print("For what it's worth, most of the days it was", atmo_mode, ".")


def main():
    parse_martian_json_data()

if __name__ == "__main__":
    main()  

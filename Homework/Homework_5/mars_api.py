import json
import requests
import statistics
<<<<<<< HEAD
import csv
=======
>>>>>>> master

"""
This program will query the MAAS2 API to pull information transmitted from the Mars
Curiosity Rover. Specifically I'd like to understand the average high and low
<<<<<<< HEAD
temperatures for the past 30 days, the maximum and mininum in the range of 30 sols,
 and the mode of the atmospheric opacity.
"""
# Assign API URL to a variable
mars_url = "https://api.maas2.apollorion.com"

# Initialize lists to use later for statistics for 3 json keys
=======
temperatures for the past 30 days, the maximum and mininum in the range of 60 sols,
 and the mode of the atmospheric opacity.
"""

# Initialize the api URL as a variable
mars_url = "https://api.maas2.apollorion.com"

# Initialize the lists to store the values pulled from the json received from API
>>>>>>> master
max_temp = []
min_temp = []
atmospheric_opacity = []

<<<<<<< HEAD
def get_sols_from_file():
    """
    Designed to open a csv file called sols.csv which will contain
    a range of comma separated sols. For example, the file I've included contains 
    the last 60 days worth of data. Just for an FYI the latest available sol we
    can query is number 2667. The function reads the file, stores and returns the 
    values as a list.
    """
    with open('sols.csv', newline='') as sols:
        query = list(csv.reader(sols))
    return query

def parse_martian_json_data(query_list):
    """
    Function takes the read csv list as input and interates over the sol values to return 
    json object for each sol. For each json object returned the next set of instructions 
    seeks specific fields within each json as it is queried and pulls the value out.
    The value is appended to the lists we initialized above.
    """
    for sol in query_list[0]:
=======
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
>>>>>>> master
        data = requests.get(mars_url + "/" + str(sol) + "/")
        json_obj = json.loads(data.text)
        
        max_temp.append(json_obj['max_temp'])
        min_temp.append(json_obj['min_temp'])
        atmospheric_opacity.append(json_obj['atmo_opacity'])

<<<<<<< HEAD
    # Here we run some basic stats on the lists we've pulled such as mean, mode, min, and max.
=======
# Calculate the statistics (mean, min, max) for temperture and mode for atmospheric opacity
>>>>>>> master
    temp_max_mean = statistics.mean(max_temp)
    max_max_temp = max(max_temp)
    temp_min_mean = statistics.mean(min_temp)
    min_min_temp = min(min_temp)
    atmo_mode = statistics.mode(atmospheric_opacity)

<<<<<<< HEAD
    # Now we're going to write out the report in a text file for the user
    # Open a new file and create some strings to contextualize the output
    with open('martian_weather_report.txt', 'w') as report:
        line_one = "The amount of sols you queried from the Curiosity data was: " 
        line_two = "The average high temperature (in Celsius): "
        line_three = "The average low temperature (in Celsius): "
        line_four = "High temperature extreme (in Celsius): "
        line_five = "Low temperature extreme (in Celsius): "
        line_six = "Most common atmospheric conditions: "
    
    #Write the above strings and their corresponding values to the report 
        report.write(line_one)
        report.write(str(len(query_list[0])))
        report.write("\n")
        report.write(line_two)
        report.write(str(temp_max_mean))
        report.write("\n")
        report.write(line_three)
        report.write(str(temp_min_mean))
        report.write("\n")
        report.write(line_four)
        report.write(str(max_max_temp))
        report.write("\n")
        report.write(line_five)
        report.write(str(min_min_temp))
        report.write("\n")
        report.write(line_six)
        report.write(atmo_mode)

def main():
    sol_range = get_sols_from_file()
    print()
    print("Please be patient, this may take some time. Pretend the Jeorpardy song is playing.")
    print()
    parse_martian_json_data(sol_range)
    print()
    print("Your report is now complete.")
    print("Please open 'martian_weather_report.txt' to view your results.")
=======
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
>>>>>>> master

if __name__ == "__main__":
    main()  

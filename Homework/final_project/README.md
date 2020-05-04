## Final Project

### Background
For my final project in DAT-129, I decided to build off the API script I developed earlier on in the
semester. Instead of the script being interactive, I wanted to focus more on the data analysis aspect.
As such this is a deviation from scripts I've written in the past that require user input or make use
of a menu.

The API I am calling doesn't appear to have its documentation hosted on the site [programmable web](https://www.programmableweb.com/api/nasas-mars-atmospheric-aggregation-system-maas-rest-api) has listed anymore but the [endpoint can be found here](https://api.maas2.apollorion.com).

### What does it do?
This script primarily focuses on distilling data and creating visualizations. But more specifically:
* Send a request to the API for data from each available sol
* Create a dataframe from the requested json objects
* Converts and writes the dataframe to a csv
* Reads the csv (to avoid calling the API too much) and creates a dataframe
* Clean the data (i.e. removing invalid requests (404) and dropping empty values (NaN))
* Extract valuable and/or interesting data
* Visualize the data in easy to read graphs and save the graphs

### Future steps?
If possible I'd like to take this same approach and use an API with more data. Even though what I have is basic tabulations and summaries of the martian weather data, I'd like to build on what I've learned and develop more complex visualizations and analytical approaches to data.
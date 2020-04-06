# API Project Notes and Instructions

## What does this program do?
Have you ever wondered what it's like on Mars in terms of weather? This API will scratch that itch!
This program queries the final 60 sols (or Martian days) of recorded data available to the MAAS2 API which is built upon
the Rover Environmental Monitoring Station (REMS). The ouput of this program is a basic statistical computation
of the various data points such as average high and low temperatures, the highest and lowest temperatures, and finally
the mode of the atmospheric opacity.

## How does it work?
This program iterates over the final 60 sol's worth of information available through the API, tracing from 2607 through
2667. Data points for temperature and opacity are pulled into individual lists as each sol is iterated over via the API.
Using some functions from the statistics module and some built in methods, the program extracts the data we want to use
and sets their output to a variable. Finally, we generate a mini weather report on the data we've queried, printed to the
screen.

## That's neat but is that all it does?
Yeah, :( but don't be so glum about it!
There are some additional fields we can extract such as UV irradiance, sunrise and sunset times (UTC), and information on
the local atmospheric pressure. We can also publish the output data to a file to save for later.
But really here the only limit to what we can do is based on the returned data from API. We can use this framework as a 
starting point and research other APIs we can use that may provide more data on Mars. But why stop there? Maybe we can 
also find something to aggregate data on the conditions of other planets.

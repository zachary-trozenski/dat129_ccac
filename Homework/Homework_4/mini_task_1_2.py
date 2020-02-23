# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 18:57:59 2020

@author: zachary.trozenski

# Mini task #1 & #2
"""   
"""
For Mini Task #2:
The plan here is to open the capital projects file as a dictionary and assign
to a variable to be parsed by a series of filters.
Once the dictionary is read from the csv, the first filter triggers which 
seeks to extract all project ids for all rows that are missing an area value 
(i.e. when the value is null). The projects which are missing an area have
their id extracted and appended to an individual text file.
The second filter then triggers to extract all project ids that do not contain 
an asset id. These project's ids are then written to a separate text file. 
Note: This second filter isn't required but I wanted to try somethat that had more
empty values than area.
"""


def dump_missing_data(incomplete_row):
    with open('incomplete_data.txt', 'a') as dumpfile:
        dumpfile.write(incomplete_row + "\n")

def dump_missing_area(no_area):
    with open('no_area.txt', 'a') as missing_area:
        missing_area.write(no_area + "\n")

def aggregate_unique(area_values):
    area_list = []
    if area_values not in area_list:
        area_list.append(area_values)
    return area_list

with open('capital_projects.csv') as projects:
    cap_proj = csv.DictReader(projects)
    area_list = []
    for rows in cap_proj:
        if rows['area'] == '':
            dump_missing_area(rows['id'])
        if rows['asset_id'] == '':
            dump_missing_data(rows['id'])
        elif rows['area'] != '':
            if rows['area'] not in area_list:
                area_list.append(rows['area'])
    for things in area_list:
        print(things)

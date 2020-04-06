# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 18:57:59 2020

@author: zachary.trozenski
"""  

"""
This program is designed to allow a user to make edits to a json object which 
will be ingested by the program as a dictionary. The values of keys in the dictionary 
will be the variables by which the data is sorted. 
The following keys will be built into the json object: 
fiscal year, start date, area, asset_type, and planning status.
"""

import json
import csv

def get_sorting_criteria():
    """
    Open an external json object and read each key value pair and return as a dictionary
    """
    with open('sort_criteria.json') as json_obj:
        json_dictionary = json.load(json_obj)
    return json_dictionary

def dump_ids(rows_of_data):
    """
    Take a list and append each list entry to an external ouput file separated by a newline
    """
    with open('relevant_projects.txt', 'a') as output:
        for ids in rows_of_data:
            output.write(ids + '\n')

def main():
    sort_crit = get_sorting_criteria()
    
    # Creating variables for each of the search criteria to use in the loop
    year = sort_crit['fiscal_year']
    start_date = sort_crit['start_date']
    area = sort_crit['area']
    asset_type = sort_crit['asset_type']
    planning_status = sort_crit['status']

    # Open the csv file containing the data as a dictionary
    with open('capital_projects.csv') as projects:
        cap_proj = csv.DictReader(projects)
        # Initialize an empty list to house the values we'll sort for
        id_list = []

        for rows in cap_proj:
            # Add projects greater than or equal to the fiscal year
            if rows['fiscal_year'] >= year:
                # Add the id to to the list if it is not already there if it is greater than or equal to the fiscal year
                if rows['id'] not in id_list:
                    id_list.append(rows['id'])
            if rows['start_date'] >= start_date:
                # Add the id to to the list if it is not already there if it is greater than or equal to start date
                if rows['id'] not in id_list:
                    id_list.append(rows['id'])
            if rows['area'] == area:
                # Add the id to to the list if it is not already there if it equals area
                if rows['id'] not in id_list:
                    id_list.append(rows['id'])
            if rows['asset_type'] == asset_type:
                # Add the id to to the list if it is not already there if it equals asset type
                if rows['id'] not in id_list:
                    id_list.append(rows['id'])
            if rows['status'] == planning_status:
                # Add the id to to the list if it is not already there if it equals status value
                if rows['id'] not in id_list:
                    id_list.append(rows['id'])

    # Dump the ids from the list into an external file       
    dump_ids(id_list)


if __name__ == "__main__":
    main()








import csv

def open_csv_file():
    """
    Open the csv file capital_projects and read with DictReader
    Return a dictionary containing the neighrborhoods
    """
    with open('capital_projects.csv') as dataset:
        data = csv.DictReader(dataset)
        data_dict = {'total_budget': 0, 'total_neighborhoods': 0}
        total_cost = 0
        neighborhoods = []
        for row in data:
            total_cost += int(row['budgeted_amount'])
            if row['neighborhood'] not in neighborhoods:
                neighborhoods.append(row['neighborhood'])
        data_dict['total_budget'] = total_cost
        total_num = len(neighborhoods)
        data_dict['total_neighborhoods'] = total_num
        
    return data_dict

def basic_stats(dictionary):
    money = dictionary['total_budget']
    places = dictionary['total_neighborhoods']
    
    average = money / places

    print("In the city of Pittsburgh, there are", places, "neighborhoods.") 
    print("From 2017 - 2019 the city has dedicated approximately {:9,.2f} dollars to capital projects.".format(money))
    print("This equates to roughly {:7,.2f} dollars per neighborhood.".format(average))

capital_projects = open_csv_file()
basic_stats(capital_projects)
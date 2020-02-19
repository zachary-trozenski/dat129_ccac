import csv

def open_csv_file():
    """
    Open the csv file capital_projects and read with DictReader
    Return a dictionary containing the neighrborhoods
    """
    with open('capital_projects.csv') as dataset:
        
        
        data = csv.DictReader(dataset)
        data_dict = {'total_budget': 0, 'total_neighborhoods': 0, 'Manchester': 0, 'Squirrel_Hill':0}
        
        
        total_cost = 0
        manchester_projects = 0
        squirrel_hill_projects = 0
        neighborhoods = []
        
        
        for row in data:
            total_cost += int(row['budgeted_amount'])
            if row['neighborhood'] not in neighborhoods:
                neighborhoods.append(row['neighborhood'])
            if row['neighborhood'] == 'Manchester':
                manchester_projects += 1
            if row['neighborhood'] == 'Squirrel Hill North' or row['neighborhood'] == 'Squirrel Hill South':
                squirrel_hill_projects += 1
        
        
        data_dict['total_budget'] = total_cost
        total_num = len(neighborhoods)
        data_dict['total_neighborhoods'] = total_num
        data_dict['Manchester'] = manchester_projects
        data_dict['Squirrel_Hill'] = squirrel_hill_projects
        
        
    return data_dict

def basic_stats(dictionary):
    money = dictionary['total_budget']
    places = dictionary['total_neighborhoods']
    manchester = dictionary['Manchester']
    squill = dictionary['Squirrel_Hill']
    
    average = money / places
    
    print()
    print("In the city of Pittsburgh, there are", places, "neighborhoods represented in the capital projects data set.") 
    print("From 2017 - 2019 the city has dedicated approximately {:9,.2f} dollars to capital projects.".format(money))
    print("This equates to roughly {:7,.2f} dollars per neighborhood.".format(average))
    print()
    print("The number of projects completed or running in the Manchester neighborhood on the North Shore are", manchester, ".")
    print("The number of projects completed or running in both sections of Squirrel Hill are", squill, ".")
    print()
    

capital_projects = open_csv_file()
basic_stats(capital_projects)
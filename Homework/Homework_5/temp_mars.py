import requests
import json

mars_url = "https://api.maas2.apollorion.com/"

json_obj = {}

list_1 = []

for sol in range(2637,2668):
    #response = requests.request("GET", mars_url + "/" + str(sol) + "/")
    response = requests.get(mars_url + str(sol) + "/")
    data = json.loads(response.text)

    print(data)

    if data['sol'] not in list_1:
        list_1.append(data['sol'])

    print(list_1)

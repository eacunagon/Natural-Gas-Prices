import csv
from datetime import date

import pandas as pd
import requests

# API Key from EIA
api_key = 'df8bc3420afaf1f07d730567179ad3e3'
# PADD Names to Label Columns  used by api data set
PADD_NAMES = ['Date', 'Price']
# Series IDs
PADD_KEY = {'Daily':'NG.RNGWHHD.D ', 'Monthly':'NG.RNGWHHD.M', 'Yearly': 'NG.RNGWHHD.A'}
# Initialize list
final_data = []

# Pull data using api
def retrieve_api_data(padd_key):
    url = 'http://api.eia.gov/series/?api_key=' + api_key + '&series_id=' + padd_key
    r = requests.get(url)
    json_data = r.json()

    if r.status_code == 200:
        print('Success!')
    else:
        print('Error')
    return json_data

#create a csv file for each data set
def get_main_csvs():
    for index, item in enumerate(PADD_KEY):
        jdata = retrieve_api_data(PADD_KEY[item])
        with open('Gas Prices '+item+'.csv', 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(PADD_NAMES)
            for row in jdata['series'][0]['data']:
                writer.writerow(row)


get_main_csvs()







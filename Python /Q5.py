## importing the required libraries
import numpy as np
import pandas as pd
import requests

## defining function
def download_and_extract(URL):
    '''
    Python Function to download the data from the given API link and 
    then extract the following data with proper formatting
    '''
    
    ## downloading the data
    response = requests.get(URL)
    data = response.json()
    
    ## list for creating structure data
    structured_data = []
    for i in data['_embedded']['episodes']:
        ## adding records one by one 
        d = {
            'id':i['id'],
            'url':i['url'],
            'name':i['name'],
            'season':i['season'],
            'number':i['number'],
            'type':i['type'],
            'airdate':i['airdate'],
            'airtime':i['airtime'],
            'airstamp':i['airstamp'],
            'runtime':i['runtime'],
            'rating':i['rating'],
            'image':i['image'],
            'summary':i['summary'],
            '_links':i['_links']
            }
        structured_data.append(d)


    ## creating dataframe and converting it into csv format
    df = pd.DataFrame(structured_data)
    df.to_csv('episodes.csv', index=False)
    
    dataset = pd.read_csv('episodes.csv')
    print(dataset.head())
    
URL = 'http://api.tvmaze.com/singlesearch/shows?q=westworld&embed=episodes'
download_and_extract(URL)
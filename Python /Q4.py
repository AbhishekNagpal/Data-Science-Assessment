## Q4
## importing the required libraries
import numpy as np
import pandas as pd
import requests

def convert_csv(URL, output):
    '''
    Python Function download the data from the link given below and then
    read the data and convert the into the proper structure and return it as 
    a CSV file.
'''
    # Downloading the data from the provided link
    response = requests.get(URL)
    data = response.json()
    
    # Create a DataFrame from the data
    df = pd.DataFrame(data)
    
    # Save the DataFrame to a CSV file
    df.to_csv(output, index=False)
    
    


URL = 'https://data.nasa.gov/resource/y77d-th95.json'
output = 'nasa_data.csv'
convert_csv(URL, output)

## now we can read the data from the csv file
##Q3
## importing the required libraries
import numpy as np
import pandas as pd
import requests

def convert_excel(URL,output):
    '''
    Python Function which would download the data from the provided link,
    and then read the data and convert that into properly structured data 
    and return it in Excel format.
    '''
    ## lets download the data the through URL 
    response = requests.get(URL)
    data = response.json()
    
    # Extract the required fields from the data and create a DataFrame
    structured_data = []
    for i in data['pokemon']:
        d = {
            'ID': i['id'],
            'Number': i['num'],
            'Name': i['name'],
            'Image URL': i['img'],
            'Type': ', '.join(i['type']),
            'Height': i['height'],
            'Weight': i['weight'],
            'Candy': i['candy'],
            'Candy Count': i.get('candy_count', ''),
            'Egg': i['egg'],
            'Spawn Chance': i.get('spawn_chance', ''),
            'Avg Spawns': i.get('avg_spawns', ''),
            'Spawn Time': i.get('spawn_time', ''),
            
            'Weakness': ', '.join(i.get('weaknesses', [])),
            'Next Evolution': ', '.join(evol['name'] for evol in i.get('next_evolution', [])),
            'Previous Evolution': ', '.join(evol['name'] for evol in i.get('prev_evolution', []))
        }
        structured_data.append(d)
    
    # Convert the structured data to a DataFrame
    df = pd.DataFrame(structured_data)
    
    # Save the DataFrame to Excel format
    df.to_excel(output, index=False)


URL = 'https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json'
output = 'pokemon_data.xlsx'
convert_excel(URL, output)


## After calling this function we can use pandas to read this file in excel format
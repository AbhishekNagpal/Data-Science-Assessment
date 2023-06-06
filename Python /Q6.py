## final functions 
## Q6
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

## Get all Pokemons that have less than 4 weaknesses
def get_pokemon_with_less_spawn_rate(file):
    df = pd.read_excel(file)
    spawn_rate_less = df[df['Spawn Chance']<0.05]
    spawn_rate_less.head()
    print(spawn_rate_less[['Name','Spawn Chance']])

    plt.figure(figsize=(12, 10))
    plt.bar(spawn_rate_less['Name'], spawn_rate_less['Spawn Chance'])
    plt.xlabel('Pokemon')
    plt.ylabel('Spawn Rate (%)')
    plt.show()
    
## Get all Pokemons that have less than 4 weaknesses
def get_pokemon_with_less_weakness(file):
    df = pd.read_excel(file)
    for i in range(len(df)):
        df['Weakness'][i] = len(df['Weakness'][i].split(','))
    less_weakness = df[df['Weakness']<4]
    print(less_weakness['Name'])
        
    plt.figure(figsize=(12, 10))
    plt.bar(less_weakness['Name'], less_weakness['Weakness'])
    plt.xlabel('Pokemon')
    plt.ylabel('Weakness')
    plt.show()
        
    

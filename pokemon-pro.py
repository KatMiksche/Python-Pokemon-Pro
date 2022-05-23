#IMPORT ALL MODULES REQUIRED
import requests
import random
import pandas as pd

# KATIE - greet player, get name and if want to generate or choose pokemons

# KATARINA  - generate list of 10 rand numbers (1-151) without duplicities
contains_duplicates=True
while contains_duplicates is not False:
    pokemon_list=random.sample(range(1,151), 10)
    print(pokemon_list)
    id_set = set(pokemon_list)
    contains_duplicates = len(pokemon_list) != len(id_set)
    print(contains_duplicates)

# if choosing pokemons, by names of pokemon find IDs from all_pokemons and overwrite first 5 entries in the list

# KATARINA - pull pokemons to 2 arrays of 5
player1 = pd.DataFrame(columns=('id', 'name', 'height','weight','hp','attack','defence','sprite'))
player2 = pd.DataFrame(columns=('id', 'name', 'height','weight','hp','attack','defence','sprite'))
for i in range (0,5):
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_list[i])
    response = requests.get(url)
    pokemon = response.json()
    pokemon_new = pd.DataFrame([[pokemon['id'], pokemon['name'], pokemon['height'], pokemon['weight'],
                pokemon['stats'][0]['base_stat'], pokemon['stats'][1]['base_stat'], pokemon['stats'][2]['base_stat'],
                pokemon['sprites']['front_default']]], columns=('id', 'name', 'height','weight','hp','attack','defence','sprite'))
    player1 = pd.concat([player1,pokemon_new], ignore_index=True)
for i in range (5,10):
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_list[i])
    response = requests.get(url)
    pokemon = response.json()
    pokemon_new = pd.DataFrame([[pokemon['id'], pokemon['name'], pokemon['height'], pokemon['weight'],
                pokemon['stats'][0]['base_stat'], pokemon['stats'][1]['base_stat'], pokemon['stats'][2]['base_stat'],
                pokemon['sprites']['front_default']]], columns=('id', 'name', 'height','weight','hp','attack','defence','sprite'))
    player2 = pd.concat([player2,pokemon_new], ignore_index=True)
print(player1)
print(player2)

# KATARINA - choose pokemon for combat round and safeguard on 0 HP for human

# KATARINA - choose pokemon for combat round and safeguard on 0 HP for computer

# KATARINA - combat round = New HP = HP - (attack-defense)

# game run - repetition of combat until all cards 0 hp

# announce result

# if win read highscores.csv to array, append new win and desc sort by win likelyhood (sum of hp+attack+defense/computer in %)
# highscores.csv - timestamp, player name, pokemons in team, opponent team, win likelyhood

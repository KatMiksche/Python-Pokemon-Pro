#IMPORT ALL MODULES REQUIRED
import requests
import random
import pandas as pd

# KATIE - greet player, get name and if want to generate or choose pokemons

# KATARINA  - generate list of 10 rand numbers (1-151) without duplicities
contains_duplicates=True
while contains_duplicates is not False:
    pokemon_list=random.sample(range(0,100), 10)
    print(pokemon_list)
    id_set = set(pokemon_list)
    contains_duplicates = len(pokemon_list) != len(id_set)
    print(contains_duplicates)

# if choosing pokemons, by names of pokemon find IDs from all_pokemons and overwrite first 5 entries in the list

# KATARINA - pull pokemons to 2 arrays of 5

# KATARINA - choose pokemon for combat round and safeguard on 0 HP for human

# KATARINA - choose pokemon for combat round and safeguard on 0 HP for computer

# KATARINA - combat round = New HP = HP - (attack-defense)

# game run - repetition of combat until all cards 0 hp

# announce result

# if win read highscores.csv to array, append new win and desc sort by win likelyhood (sum of hp+attack+defense/computer in %)
# highscores.csv - timestamp, player name, pokemons in team, opponent team, win likelyhood

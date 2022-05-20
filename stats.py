import requests
import matplotlib.pyplot
import pandas as pd
pokemon_list=pd.DataFrame(columns=('id', 'name', 'height','weight','hp','attack','defence','sprite'))
for i in range(1,152):
  url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(i)
  response = requests.get(url)
  pokemon = response.json()
  pokemon_new = pd.DataFrame([[pokemon['id'], pokemon['name'], pokemon['height'], pokemon['weight'],
                pokemon['stats'][0]['base_stat'], pokemon['stats'][1]['base_stat'], pokemon['stats'][2]['base_stat'],
                pokemon['sprites']['front_default']]], columns=('id', 'name', 'height','weight','hp','attack','defence','sprite'))
  pokemon_list = pd.concat([pokemon_list,pokemon_new], ignore_index=True)
print(pokemon_list)
pokemon_list.to_csv('all_pokemons.csv', index=False)
plot_list = pd.DataFrame(pokemon_list)
plot_list = plot_list.drop(['id', 'name', 'height','weight','sprite'], axis=1)
print(plot_list)
matplotlib.pyplot.boxplot(plot_list, labels=('hp','attack','defence'))



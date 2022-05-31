#IMPORT ALL MODULES REQUIRED
import requests
import random
import pandas as pd
from datetime import datetime
from tkinter import *
from PIL import ImageTk,Image
import io
import urllib.request





# Syeda Create an instance of tkinter window
win = Tk()
win.title("pokemon Game")
win.configure(background="turquoise")

# Define the geometry of the window
win.geometry("700x500")

frame = Frame(win, width=600, height=400)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

# Create an object of tkinter ImageTk
img = ImageTk.PhotoImage(Image.open("C:\\Users\\syeda shah\\Python-Pokemon-Pro-main-update\\pokemoncards\\start.png"))

# Create a Label Widget to display the text or Image
label = Label(frame, image = img)
label.pack()

player_name = Label(win, text='what is your name? ')
player_name.pack()


def printInput():
    inp = inputtxt.get(1.0, "end-1c")
    lbl.config(text="Player name: " + inp)


# TextBox Creation
inputtxt = Text(win,
                height=2,
                width=10)

inputtxt.pack()

# Button Creation
printButton = Button(win,
                     text="Enter",
                     command=printInput)
printButton.pack()

# Label Creation
lbl = Label(win, text="", background="turquoise")
lbl.pack()


def play_button():
    frame2 = Frame(win, width=800, height=700,background="turquoise")
    frame2.pack()
    frame2.place(anchor='center', relx=0.5, rely=0.5)


    contains_duplicates = True
    while contains_duplicates is not False:
        pokemon_list = random.sample(range(1, 151), 10)
        lbl2 = Label(win, text=pokemon_list, background="turquoise")
        lbl2.pack()

        id_set = set(pokemon_list)
        contains_duplicates = len(pokemon_list) != len(id_set)

        # KATARINA - pull pokemons to 2 arrays of 5
        player1 = pd.DataFrame(columns=('id', 'name', 'height', 'weight', 'hp', 'attack', 'defence', 'sprite'))
        player2 = pd.DataFrame(columns=('id', 'name', 'height', 'weight', 'hp', 'attack', 'defence', 'sprite'))
        for i in range(0, 5):
            url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_list[i])
            response = requests.get(url)
            pokemon = response.json()
            pokemon_new = pd.DataFrame([[pokemon['id'], pokemon['name'], pokemon['height'], pokemon['weight'],
                                         pokemon['stats'][0]['base_stat'], pokemon['stats'][1]['base_stat'],
                                         pokemon['stats'][2]['base_stat'],
                                         pokemon['sprites']['front_default']]],
                                       columns=('id', 'name', 'height', 'weight', 'hp', 'attack', 'defence', 'sprite'))
            player1 = pd.concat([player1, pokemon_new], ignore_index=True)
        for i in range(5, 10):
            url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_list[i])
            response = requests.get(url)
            pokemon = response.json()
            pokemon_new = pd.DataFrame([[pokemon['id'], pokemon['name'], pokemon['height'], pokemon['weight'],
                                         pokemon['stats'][0]['base_stat'], pokemon['stats'][1]['base_stat'],
                                         pokemon['stats'][2]['base_stat'],
                                         pokemon['sprites']['front_default']]],
                                       columns=('id', 'name', 'height', 'weight', 'hp', 'attack', 'defence', 'sprite'))
            player2 = pd.concat([player2, pokemon_new], ignore_index=True)
        lbl3 = Label(win, text="Your team", background="turquoise")
        lbl3.pack()
        lbl4 = Label(win, text=player1.iloc[0:5,0:7], background="turquoise")
        lbl4.pack()
        lbl5 = Label(win, text="Opponents team", background="turquoise")
        lbl5.pack()
        lbl6 = Label(win, text=player2.iloc[0:5, 0:7], background="turquoise")
        lbl6.pack()
       # print('\n\nYour team\n', player1.iloc[0:5, 0:7])
       # print('\n\nOpponents team\n', player2.iloc[0:5, 0:7])
        cols = ['hp', 'attack', 'defence']
        df1 = player1[cols].sum(axis=0)
        df2 = player2[cols].sum(axis=0)
        chance_to_win = round(df1.sum(axis=0) / df2.sum(axis=0), 3) * 100
        lbl5 = Label(win, text="chance to win is", background="turquoise")
        lbl5.pack()
        lbl6 = Label(win, text=chance_to_win, background="turquoise")
        lbl6.pack()
        #print('chance to win is ', chance_to_win, '%')


        def battle_button():

         while player1['hp'].sum(axis=0) > 0 and player2['hp'].sum(axis=0):
            # HERE GOES THE CODE FOR CHOOSING CARDS AND BATTLE ROUNDS

            # KATARINA - choose pokemon for combat round and safeguard on 0 HP for computer
            alive = False
            while alive is not True:
                p2 = random.randint(0, 4)
                if player2.loc[p2, 'hp'] > 0: alive = True
            lbl5 = Label(win, text="Opponents pokemon", background="turquoise")
            lbl5.pack()
            lbl6 = Label(win, text=player2.loc[p2, 'name'], background="turquoise")

            lbl6.pack()
            url = player2.loc[p2, 'sprite']





            my_label = Label(win,text=url)
            my_label.pack()

            # print('\n\nOpponents pokemon\n', player2.loc[p2])
            # url = player2.loc[p2, 'sprite']
            # text = player2.loc[p2, 'name']
            # text2 = player2.iloc[p2, 1:7]

            battle_button = Button(frame2, padx=8, width=10, pady=8, bd=8, font=("Arial",
                                                                            16), text="Battle", command=battle_button)
            battle_button.pack()





play_button = Button(win, padx=8, width=18, pady=8, bd=8, font=("Arial",26), text="Play Game", command=play_button)
play_button.pack()

win.mainloop()




# KATIE - greet player, get name and if want to generate or choose pokemons
player_name=input('what is your name? ')

# KATARINA  - generate list of 10 rand numbers (1-151) without duplicities
contains_duplicates=True
while contains_duplicates is not False:
    pokemon_list=random.sample(range(1,151), 10)
    print(pokemon_list)
    id_set = set(pokemon_list)
    contains_duplicates = len(pokemon_list) != len(id_set)



# KATIE - if choosing pokemons, by names of pokemon find IDs from all_pokemons and overwrite first 5 entries in the list

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
print ('\n\nYour team\n',player1.iloc[0:5,0:7])
print (player1.loc[player1,'name'])
print ('\n\nOpponents team\n',player2.iloc[0:5,0:7])
cols = ['hp', 'attack', 'defence']
df1 = player1[cols].sum(axis=0)
df2 = player2[cols].sum(axis=0)
chance_to_win=round(df1.sum(axis=0)/df2.sum(axis=0),3)*100
print('chance to win is ',chance_to_win,'%')

# KATARINA - game run - repetition of combat until all cards 0 hp
while player1['hp'].sum(axis=0)>0 and player2['hp'].sum(axis=0):
    # HERE GOES THE CODE FOR CHOOSING CARDS AND BATTLE ROUNDS

# KATARINA - choose pokemon for combat round and safeguard on 0 HP for computer
    alive = False
    while alive is not True:
        p2 = random.randint(0, 4)
        if player2.loc[p2, 'hp'] > 0: alive = True
    print('\n\nOpponents pokemon\n', player2.loc[p2])
    url=player2.loc[p2,'sprite']
    text=player2.loc[p2,'name']
    text2=player2.iloc[p2,1:7]


# KATARINA - choose pokemon for combat round and safeguard on 0 HP for human
    alive = False
    while alive is not True:
        p1=int(input('What pokemon do you want to play? 1/2/3/4/5 '))-1
        if p1>-1 and p1<5:
            if player1.loc[p1,'hp']>0:
                alive=True
                print ('You chose ',player1.loc[p1,'name'])
            else: print ('You need to choose pokemon capable of combat.')
        else: print('You need to choose from numbers 1 to 5')
    print('\n\nYour pokemon\n', player1.loc[p1])
    #graphics your pokemon
    #graphics button

    # KATARINA - combat round = New HP = HP - (attack-defense)

    if player1.loc[p1,'attack']>player2.loc[p2,'defence']:
        residual=player1.loc[p1,'attack']-player2.loc[p2,'defence']
        player2.iat[p2,player2.columns.get_loc('defence')]=0
        player2.iat[p2,player2.columns.get_loc('hp')]=player2.loc[p2,'hp']-residual
    else:
        player2.iat[p2,player2.columns.get_loc('defence')]=player2.loc[p2,'defence']-player1.loc[p1,'attack']
    if player2.loc[p2,'hp']<0: player2.iat[p2,player2.columns.get_loc('hp')]=0
    if player2.loc[p2,'attack']>player1.loc[p1,'defence']:
        residual=player2.loc[p2,'attack']-player1.loc[p1,'defence']
        player1.iat[p1,player1.columns.get_loc('defence')]=0
        player1.iat[p1,player1.columns.get_loc('hp')]=player1.loc[p1,'hp']-residual
    else:
        player1.iat[p1,player1.columns.get_loc('defence')]=player1.loc[p1,'defence']-player2.loc[p2,'attack']
    if player1.loc[p1,'hp']<0: player1.iat[p1,player1.columns.get_loc('hp')]=0
    print('\n\nYour team\n', player1.iloc[0:5, 0:7])
    print('\n\nOpponents team\n', player2.iloc[0:5, 0:7])

# announce result
if player1['hp'].sum(axis=0)<player2['hp'].sum(axis=0):
    print('\n\nUnfortunatelly your team lost')
else:
    print('\n\nYour team won! \nCheck the highscores.csv!')

# if win read highscores.csv to array, append new win and desc sort by win likelyhood (var chance_to_win = sum of hp+attack+defense/computer in %)
# highscores.csv - timestamp, player name, pokemons in team, opponent team, win likelyhood
    scores=pd.read_csv(r"C:\Users\Kat\PycharmProjects\pythonProject\highscores.csv") #CHANGE THE LOCATION OF FILE

    list=player1['name'].to_list()
    pok1=' '.join(list)
    list=player2['name'].to_list()
    pok2=' '.join(list)

    # source https://www.programiz.com/python-programming/datetime/strftime
    now = datetime.now() # current date and time
    year = now.strftime("%Y")
    month = now.strftime("%m")
    day = now.strftime("%d")
    time = now.strftime("%H:%M:%S")
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

    result=[date_time, player_name, pok1, pok2, chance_to_win]
    print(result)
    new_score = pd.DataFrame([result], columns=['Timestamp', 'Player_name', 'Pokemons_in_team', 'Opponent_team', 'Win_likelyhood'])
    scores=pd.concat([scores, new_score], ignore_index=True)
    scores=scores.sort_values(by=['Win_likelyhood'])
    print(scores)
    scores.to_csv(r"C:\Users\Kat\PycharmProjects\pythonProject\highscores.csv", index=False) #CHANGE THE LOCATION OF FILE

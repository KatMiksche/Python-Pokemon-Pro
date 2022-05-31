#IMPORT ALL MODULES REQUIRED
import requests
import random
import pandas as pd
import csv
from datetime import datetime
from tkinter import *
from PIL import ImageTk,Image

# SYEDA - graphics
# Create an instance of tkinter window
win = Tk()
win.title("pokemon Game")
win.configure(background="turquoise")
win.geometry("1100x700")

frm_start = Frame(win, width=900, height=500)
frm_start.place(anchor='center', relx=0.5, rely=0.5)
frm_start.pack()

# Create an object of tkinter ImageTk
img = ImageTk.PhotoImage(Image.open("start.png"))

# Create a Label Widget to display the text or Image
lbl_image = Label(frm_start, image = img)
lbl_image.pack()

lbl_pname = Label(frm_start, text='what is your name? ', font=('Times 14'))
lbl_pname.pack()

# TextBox Creation
ent_pname = Entry(frm_start,  width=10, font=('Times 14'))
ent_pname.pack()

def printInput():
    global player_name
    player_name = ent_pname.get()
    lbl_outputname.config(text="Welcome to the game, " + player_name)

# Button Creation
btn_entername = Button(frm_start, text="Enter", font=('Times 14'), command=printInput)
btn_entername.pack()

# Label Creation
lbl_outputname = Label(frm_start, text="", background="turquoise", font=('Times 14'))
lbl_outputname.pack()

def play_button():
    win.destroy()

btn_play = Button(frm_start, padx=8, width=18, pady=8, bd=8, font=("Arial", 26), text="Play Game", command=play_button)
btn_play.pack()

win.mainloop()

# KATARINA - generate list of 10 randoms IDs
contains_duplicates = True
while contains_duplicates is not False:
    pokemon_list = random.sample(range(1, 151), 10)
    id_set = set(pokemon_list)
    contains_duplicates = len(pokemon_list) != len(id_set)

# KATIE/KATARINA - if choosing pokemons, by names of pokemon find IDs from all_pokemons and overwrite first 5 entries in the list
answer=False
while answer==False:
    choice=input('Do you want to get random pokemons or choose them by names? random/choose')
    if choice=='random':
        answer=True
    elif choice=='choose':
        answer=True
        def id_name(player_input):
            player_input = player_input.lower()
            id=0
            with open(r"C:\Users\Kat\PycharmProjects\pythonProject\all_pokemons.csv", "r") as all_pokemon:
                file = csv.reader(all_pokemon)
                for row in file:
                    if row[1].lower() == player_input:
                        id=int(row[0])
            return id

        for i in range(5):
            valid=False
            while valid==False:
                player_input=input('what is the pokemon name? ')
                np_id=0
                np_id=id_name(player_input)
                if np_id>0:
                    pokemon_list[i]=np_id
                    valid=True
                else:
                    print('that is not valid name of pokemon, try again.')
        print(pokemon_list)

        contains_duplicates=True
        while contains_duplicates is not False:
            pokemon_list[5:9]=random.sample(range(1,151), 5)
            pokemon_list.pop(10)
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

print('\n\nYour team\n', player1.iloc[0:5, 0:7])
print('\n\nOpponents team\n', player2.iloc[0:5, 0:7])
cols = ['hp', 'attack', 'defence']
df1 = player1[cols].sum(axis=0)
df2 = player2[cols].sum(axis=0)
chance_to_win = round(df1.sum(axis=0) / df2.sum(axis=0), 3) * 100
print('chance to win is ', chance_to_win, '%')

# KATARINA - game run - repetition of combat until all cards 0 hp
while player1['hp'].sum(axis=0)>0 and player2['hp'].sum(axis=0):
    # HERE GOES THE CODE FOR CHOOSING CARDS AND BATTLE ROUNDS

# KATARINA - choose pokemon for combat round and safeguard on 0 HP for computer
    alive = False
    while alive is not True:
        p2 = random.randint(0, 4)
        if player2.loc[p2, 'hp'] > 0: alive = True
    print('\n\nOpponents pokemon\n', player2.loc[p2])

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

# KATARINA - announce result
if player1['hp'].sum(axis=0)<player2['hp'].sum(axis=0):
    print('\n\nUnfortunatelly your team lost')
else:
    print('\n\nYour team won! \nCheck the highscores.csv!')

# KATARINA - if win read highscores.csv to array, append new win and desc sort by win likelyhood (var chance_to_win = sum of hp+attack+defense/computer in %)
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

    # SYEDA -  Create an instance of tkinter window & end messages
    win = Tk()
    win.title("pokemon Game")
    win.configure(background="turquoise")
    win.geometry("1100x700")

    img = ImageTk.PhotoImage(Image.open("start.png"))
    lbl_image = Label(win, image=img)
    lbl_image.pack()
    praise = 'Well done, ' + player_name + '!!!'
    lbl_praise = Label(win, text=praise, background="turquoise", font=("Arial", 18), pady=5)
    lbl_praise.pack()
    lbl_winmessage = Label(win, text="\n\nYour team won! \nCheck the highscores.csv!", font=("Arial", 14), background="turquoise")
    lbl_winmessage.pack()

    def quit():
        win.destroy()

    btn_quit = Button(win, padx=8, width=18, pady=8, bd=8, font=("Arial", 14), text="Quit Game", command=quit)
    btn_quit.pack()

    win.mainloop()
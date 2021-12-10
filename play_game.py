#module is extraneous; kept here for organization (these functions are only active in fish.py)

import os
from .game_setup import *
from .fish import *

##### Pursuing a widget: gameplay 
os.system('clear')
make_barrel(barrel_waves)

#player takes turn by inputting in textbox
def play():
    '''
    a function that plays the game!
    '''
    print('Welcome to BATTLEFISH!', '\nYou lead an interesting life, and the choices you’ve made have resulted in your owning a machine gun and a lot of illegal fish.','\nHurry! You have to kill all of the fish in your barrel before the FDA, EPA, and SWAT team bust you! You don’t know where they are, and you only have 40 bullets in your gun. Good luck.')
    for i in range(player_turns):
        print("Bullets used:", i + 1, "of", player_turns)
        print("Fish left:", len(fishies))
        print()

        user_guess = {}
        while True:
            user_guess['row'] = input_row()
            user_guess['col'] = input_col()
            #accounting for reduncancy because users will give bad input
            if barrel_waves[user_guess['row']][user_guess['col']] == 'X' or barrel_waves[user_guess['row']][user_guess['col']] == '#':
                    print("\nYou've already shot there; try again")
            else:
                break

        os.system('clear')
    #when the fish are hit
        strike = False
        for i in fishies:
            if i.hit(user_guess):
                print("\nYou hit one!")
                strike = True
                barrel_waves[user_guess['row']][user_guess['col']] = 'X'
                if i.sunk():
                    print("\nSPLAT! You killed a fish.")
                    fishies.remove(i)
                    #else:
                        #target fish by hitting around this spot
                break
    #when the fish are missed
        if not strike:
            barrel_waves[user_guess['row']][user_guess['col']] = '#'
            print("\nYou missed.")

        make_barrel(barrel_waves)

        if not fishies:
            break
play()
if fishies:
    print("You didn't kill the fish in time, so you got arrested and sent to fish-smuggler jail :(")
else:
    print("You killed all the fish and destroyed the evidence! Your fish-smuggling operation is safe... for now")
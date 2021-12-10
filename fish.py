from .game_setup import *
import os

fishies = []
class Fish():
    def __init__(self, length, pos, loc):
        '''
        A function to initialize the positions of the fish
        '''
        self.length = length
        if pos == 'horizontal' or pos == 'vertical':
            self.pos = pos #make position/orientation of fish horizontal or vertical
        else:
            print('fish must be oriented horizontally or vertically')
        
        if pos == 'horizontal':
            if loc['row'] in range(num_row):
                self.coords = []
                for i in range(length):
                    if loc['col'] + i in range(num_col):
                        self.coords.append({'row': loc['row'], 'col': loc['col'] + i})
                    else:
                        print('column out of range') #make raise error statement not print
                else:
                    print('row out of range') #make raise error statement not print
                    
        if pos == 'vertical':
            if loc['row'] in range(num_col):
                self.coords = []
                for i in range(length):
                    if loc['col'] + i in range(num_row):
                        self.coords.append({'row': loc['row'] + i, 'col': loc['col']})
                    else:
                        print('row out of range') #make raise error statement not print
                else:
                    print('column out of range') 
                    
                    if self.already_placed():
                        make_barrel(barrel)
                        print(" ".join(str(i) for i in self.coords))
                        raise IndexError("fish already there")
                    else:
                        self.place_fish()
  
  
    def already_placed(self):
        '''
        A function that prevents the fish from being redundantly placed
        '''
        for i in self.coords:
            if barrel[i['row']][i['col']] == 1:
                return True
    
    def place_fish(self):
        '''
        A function that places the fish
        '''
        for i in self.coords:
            barrel[i['row']][i['col']] = 1
               
    def hit(self, loc):
        '''
        A function that determines a hit
        '''
        for i in self.coords:
            if i == loc:
                return True

    def sunk(self):
        '''
        A function that checks if the fish has been destroyed (cannot be - or # on the board)
        '''
        for i in self.coords:
            if barrel_waves[i['row']][i['col']] == '-':
                return False
            elif barrel_waves[i['row']][i['col']] == '#':
                print("whoopsie")
        return True
                
#making the fish components: use class
a = 0 #temporary variable
while a < num_fish: 
    fish_input = rand_locs()

    fishies.append(Fish(fish_input['length'], fish_input['orientation'], fish_input['location']))
    a += 1
del a #delete temporary variable

######################################

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
from random import randint

#game board dimensions
num_row = 8 
num_col = 8
num_fish = 4
player_turns = 40
max_fish_length = 5
min_fish_length = 2

#initial board
barrel = [[0] * num_col for i in range(num_row)]
barrel_waves = [["-"] * num_col for i in range(num_row)]

#functions to make board
#add and subtract all these 1s to account for the boarder that marks columns/rows
def make_barrel(barrel_grid):
    '''
    A function that makes the board on which the user plays the game
    '''
    print("\n  " + " ".join(str(i) for i in range(1, num_col + 1)))
    for j in range(num_row):
        print(str(j + 1) + " " + " ".join(str(k) for k in barrel_grid[j]))

#placing the fish in the barrel for the user to strike
def locs(length, pos):
    '''
    A function that finds viable locations for the fish
    '''
    loc = []

    if pos != 'horizontal' and pos != 'vertical':
        print("Fish must be horizontal or vertical")

    if pos == 'horizontal':
        if length <= num_col:
            for i in range(num_row):
                for j in range(num_col - length + 1):
                    if 1 not in barrel[i][j:j+length]:
                        loc.append({'row': i, 'col': j}) #dictionary 
            
    if pos == 'vertical':
        if length <= num_row:
            for j in range(num_col):
                for i in range(num_row - length + 1):
                    if 1 not in [barrel[k][j] for k in range(i, i+length)]:
                        loc.append({'row': i, 'col': j})

    if not loc:
        return 'None'
    else:
        return loc

def rand_locs():
    '''
    A function that picks random locations for the fish that the user must strike
    '''
    length = randint(min_fish_length, max_fish_length) 
    pos = 'horizontal' if randint(0, 1) == 0 else 'vertical' #decide fish orientation

    loc = locs(length, pos)
    if loc == 'None':
        return 'None'
    else:
        return {'location': loc[randint(0, len(loc) - 1)], 'length': length, 'orientation': pos}

#user input ship position coordinates by row and column
def input_col():
    '''
    A function that allows the user to input a guess for the column
    '''
    while True:
        try:
            guess = int(input("Column Guess: "))
            if guess in range(1, num_col + 1):
                return guess - 1
            else:
                print("\nSilly goose! You missed the barrel! Try again")
        except ValueError:
            print("\nThat's not a number, silly goose.")

def input_row():
    '''
    A function that allows the user to input a guess for the row
    '''
    while True:
        try:
            guess = int(input("Row Guess: "))
            if guess in range(1, num_row + 1):
                return guess - 1
            else:
                print("\nSilly goose! You missed the barrel! Try again")
        except ValueError:
            print("\nThat's not a number, silly goose.")
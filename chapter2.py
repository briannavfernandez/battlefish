import random

#chapter 2 

length = [2,3,3,4,5]  
player_barrel = [["-"] * 8 for i in range(8)]
ai_barrel = [["-"] * 8 for i in range(8)]

player_barrel_turn = [["-"] * 8 for i in range(8)]
ai_barrel_turn = [["-"] * 8 for i in range(8)]

make_letters = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7}

#making the board
def make_board(board):
    '''
    A function that makes the game board (improved from chapter 1)
    '''
    print("  A B C D E F G H")
    print("  ---------------")
    num_row = 1
    for row in board:
        print("%d|%s|" % (num_row, "|".join(row)))
        num_row += 1
        
        
#these functions used to be in the class structure, but have been removed and modified for chapter 2
def check_fish_fit(fish_length, row, col, pos):
    '''
    A function that checks if the fish fits on the barrel board
    '''
    if pos == "H":
        if col + fish_length > 8:
            return False
        else:
            return True
    else:
        if row + fish_length > 8:
            return False
        else:
            return True

def fish_overlaps(board, row, col, pos, fish_length):
    '''
    A function that checks the location of each fish for overlap
    '''
    if pos == "H":
        for i in range(col, col + fish_length):
            if board[row][i] == "X":
                return True
    else:
        for i in range(row, row + fish_length):
            if board[i][col] == "X":
                return True
    return False

def user_input(place_fish):
    '''
    A function that takes user input for placing and striking fish
    '''
    if place_fish == True:
        while True:
            try: 
                pos = input("Enter orientation (H or V): ").upper()
                if pos == "H" or pos == "V":
                    break
            except TypeError:
                print('Enter a valid orientation H or V')
        while True:
            try: 
                row = input("Enter the row (1-8) of the fish: ")
                if row in '12345678':
                    row = int(row) - 1
                    break
            except ValueError:
                print('Enter a valid letter between 1-8')
        while True:
            try: 
                col = input("Enter the column of the fish: ").upper()
                if col in 'ABCDEFGH':
                    col = make_letters[col]
                    break
            except KeyError:
                print('Enter a valid letter between A-H')
        return row, col, pos 
    else:
        while True:
            try: 
                row = input("Enter the row (1-8) of the fish: ")
                if row in '12345678':
                    row = int(row) - 1
                    break
            except ValueError:
                print('Enter a valid letter between 1-8')
        while True:
            try: 
                col = input("Enter the column of the fish: ").upper()
                if col in 'ABCDEFGH':
                    col = make_letters[col]
                    break
            except KeyError:
                print('Enter a valid letter between A-H')
        return row, col       

def place_fish(board):
    '''
    a function that places the fish on the barrel board, looping through the different lengths of fish to do so for both the computer and the player
    '''

    for fish_length in length:
        #loop to fins when the fish fits in the barrel without overlap 
        while True:
            if board == ai_barrel:
                pos, row, col = random.choice(["H", "V"]), random.randint(0,7), random.randint(0,7)
                if check_fish_fit(fish_length, row, col, pos):
                    #check if fish overlaps
                    if fish_overlaps(board, row, col, pos, fish_length) == False:
                        #place fish
                        if pos == "H":
                            for i in range(col, col + fish_length):
                                board[row][i] = "X"
                        else:
                            for i in range(row, row + fish_length):
                                board[i][col] = "X"
                        break
                        
            
            else:
                place_fish = True
                print('\nPlace your ' + str(fish_length) + '-block long fish:')
                row, col, pos = user_input(place_fish)
                if check_fish_fit(fish_length, row, col, pos):
                    #check if fish overlaps
                        if fish_overlaps(board, row, col, pos, fish_length) == False:
                            #place fish
                            if pos == "H":
                                for i in range(col, col + fish_length):
                                    board[row][i] = "X"
                            else:
                                for i in range(row, row + fish_length):
                                    board[i][col] = "X"
                            make_board(player_barrel)
                            break 

def hit(board):
    '''
    A function that checks if the fish are hit and counts it
    '''
    hit_fish = 0
    for row in board:
        for col in row:
            if col == "X":
                hit_fish += 1
    return hit_fish



#user and computer turn - gameplay
def play(board):
    '''
    A function that plays the game by giving the player and the computer turns 
    '''
    if board == player_barrel_turn:
        row, col = user_input(player_barrel_turn)
        if board[row][col] == "#":
            play(board)
        elif board[row][col] == "X":
            play(board)
        elif ai_barrel[row][col] == "X":
            board[row][col] = "X"
        else:
            board[row][col] = "#"
            
#computer's turn: random strikes
    else:
        row, col = random.randint(0,7), random.randint(0,7) 
        if board[row][col] == "#":
            play(board)
        elif board[row][col] == "X":
            play(board)
        elif player_barrel[row][col] == "X":
            board[row][col] = "X"
        else:
            board[row][col] = "#"

#title card and display computer's board/barrel and make random placements           
print('\nWelcome to BATTLEFISH: Chapter 2','\nYou promised yourself you’d quit, but you’ve fallen back into smuggling illegal fish. However, this time you have competition.''\nAnother smuggler is planning to shoot all of your fish to get you out of the game. Quick, shoot his first, so he loses inventory and goes bankrupt!')
print('\nHis barrel:')
make_board(ai_barrel)
place_fish(ai_barrel)

#start with blank board that the player will be using
print('\nYour barrel:')
make_board(player_barrel)
place_fish(player_barrel)
        
while True:
    #player turn
    while True:
        print('\nGuess a location:')
        make_board(player_barrel_turn)
        play(player_barrel_turn)
        break
    if hit(player_barrel_turn) == 17:
        print("You shot all of the other smuggler's fish! Now he has become bankrupt and starving while your business grows")
        break   
    #computer turn
    while True:
        play(ai_barrel_turn)
        break           
    make_board(ai_barrel_turn)   
    if hit(ai_barrel_turn) == 17:
        print("The other smuggler shot all of your fish and is now stealing your corner of the illegal fish market :/")
        break
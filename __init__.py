from .game_setup import *
from .fish import *

part2 = input("Ready for Chapter 2? Y or N?").upper()
if part2 == 'Y':
    from .chapter2 import * 
else:
    print("\nThanks for playing!")
import random
from dice import *
from posibility_count import *
from scoreboard import *
from scoring import *

def menu():
    # Initial roll
    cast0 = diceroll([])
    throws = 0
    while throws < 2:
        
        print(f"Current roll: {cast0}")
        
        
        selection = input("Which dice do you want to reroll? (Enter positions separated by spaces, or 'n' for no rerolls): ")
        
        if selection.lower() == 'n':
            print("No rerolls selected.")
            posibilities(cast0)
            chosencategory = input("Where do you want to put your score: ")
            break

        # Get the indices for dice to reroll
        replace_indices = list(map(int, selection.split()))
        for i in replace_indices:
            cast0[i - 1] = 9  # Mark dice to reroll with 9

        # Reroll the selected dice
        cast0 = diceroll(cast0)
        throws += 1
        print(f"Your cast: {cast0}")
        posibilities(cast0)

menu()
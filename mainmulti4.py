from dice import *
from posibility_count import *
from scoreboard import *
from scoring import *

def categorychoice(filledcategories, cast):
    categories = ["ones", "twos", "threes", "fours", "fives", "sixes",
                  "one pair", "two pairs", "three of a kind", "four of a kind",
                  "small straight", "large straight", "full house", "chance", "yatzy"]
    
    category = input('Enter a category: ').strip().lower()
    if category in filledcategories:
        return 'This category is filled; choose a different one'
    if category not in categories:
        return 'Invalid category; try again'
    try:
        score = scorecalculation(category, cast)
        filledcategories[category] = int(score)
        return f'You scored {score} points in the {category}', filledcategories
    except (ValueError, TypeError):
        return 'Type error or value error; try again'
    
    
def menu():
    nplayers = int(input('Enter the number of players: '))
    playernames = []
    playerscore = {}   # CHANGED: Now stores each player's scores separately
    totalscore = {}    # CHANGED: Stores each player's total score separately
    filledcategories = {}  # ADDED: Separate filled categories for each player

    # Initialize each player's data
    for player in range(nplayers):
        name = input(f'Enter a name for player {player + 1}: ')
        playernames.append(name)
        playerscore[name] = {}  # CHANGED: Each player has their own score dictionary
        totalscore[name] = 0  # CHANGED: Each player starts with a score of 0
        filledcategories[name] = {}  # ADDED: Each player has their own category tracking

    # Main game loop
    while any(len(filledcategories[player]) < 15 for player in playernames):  # CHANGED: Checks if each player has filled 15 categories
        for player in playernames:
            print(f'\n{player}\'s TURN')
            cast0 = diceroll([])
            throws = 0
            while throws < 2:
                print(f"Current roll: {cast0}")
                
                selection = input("Which dice do you want to reroll? (Enter positions separated by spaces, or 'n' for no rerolls): ")
                if selection.lower() == 'n':
                    print("No rerolls selected.")
                    posibilities(cast0)
                    break

                replace_indices = list(map(int, selection.split()))
                for i in replace_indices:
                    cast0[i - 1] = 9  # Mark dice to reroll with 9

                cast0 = diceroll(cast0)
                throws += 1
                print(f"Your cast: {cast0}")
                posibilities(cast0)
                
            while True:
                result = categorychoice(filledcategories[player], cast0)  # CHANGED: Passes individual player's filled categories
                if isinstance(result, str):
                    print(result)
                else:
                    message, updated_categories = result
                    print(message)
                    filledcategories[player] = updated_categories  # CHANGED: Updates individual player's filled categories
                    break

            for category, score in filledcategories[player].items():  # CHANGED: Loops over the specific player's categories
                playerscore[player][category] = score  # CHANGED: Updates the specific player's score
                totalscore[player] = sum(playerscore[player].values())  # CHANGED: Updates the specific player's total score
            
            print(f'\nSCOREBOARD for {player}')
            print(displayscoreboard(filledcategories[player]))  # CHANGED: Displays the specific player's scoreboard
            print(f"Your current total score: {totalscore[player]}")  # CHANGED: Displays the specific player's total score
        
    # Calculate bonuses and final scores
    for player in playernames:
        bonus = bonuscheck(playerscore[player])  # CHANGED: Checks bonus for each player separately
        totalscore[player] += bonus  # CHANGED: Adds bonus to the specific player's total
        print(f'{player} receives {bonus} points as bonus')
    
    print('\nFINAL SCORES:')
    for player in playernames:
        print(f'{player}: {totalscore[player]}')  # CHANGED: Displays each player's final total score

menu()

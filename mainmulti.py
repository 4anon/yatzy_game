from dice import *
from posibility_count import *
from scoreboard import *
from scoring import *


def categorychoice(filledcategories,cast):
    categories=[ "ones", "twos", "threes", "fours", "fives", "sixes",
        "one pair", "two pairs", "three of a kind", "four of a kind",
        "small straight", "large straight", "full house", "chance", "yatzy"]
    
    category=input('enter a category: ').strip().lower()
    if category in filledcategories:
        return 'this category is filled choose a different one'
    if category not in categories:
        return 'invalid category try again'
    try:
        score=scorecalculation(category,cast)
    
        filledcategories[category]=int(score)
        return f'You scored {score} points in the {category}',filledcategories
    except (ValuError,TypeError):
        return'Type error or Value error try again'
    
    
def menu():
    filledcategories={}
    totalscore={}
    nplayers=int(input('enter the number of players:'))
    playerscore={}
    playerboard={}
    for player in range(nplayers):
        playerscore[player]=0
        playerboard[player]={}
    for player in range(nplayers):
        totalscore[player]=0
 
    while len(filledcategories)<15:
        for player in range(nplayers):
            print(f'\n {player}s TURN')
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
            print(displayscoreboard(filledcategories))
            while True:
                result=categorychoice(filledcategories,cast0)
                if result[0]:
                    print(result[0])
                else:
                    filledcategories=result[1]
             
                if filledcategories:
                    for placement in filledcategories:
                        category=placement
                    score=filledcategories[category]
                    totalscore[player]+=score
                    print(f'category:{category} ,score:{score}')
                    break
                else:
                    print('Either all categories are filled or invalid category.')
        print(displayscoreboard(filledcategories))
        print(f'Your current total score is:{totalscore}')    
    print('\n FINAL SCORES:')
    for player in range(nplayers):
        print(f'player{player}:{totalscore[player]}')
    

menu()

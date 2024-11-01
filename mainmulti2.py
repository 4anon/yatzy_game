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
    except (ValueError,TypeError):
        return'Type error or Value error try again'
    
    
def menu():
    filledcategories={}
    totalscore={}
    nplayers=int(input('enter the number of players:'))
    playerscore={}
    playernames=[]
    for player in range(nplayers):
        name=input(f'Enter a name for player {player}: ')
        playernames.append(name)
        playerscore[player]={}
        totalscore[player]=0
    #DEBUG global highscorename,highscorevalue
    #DEBUG highscorename,highscorevalue=highscoreinstall()
    while len(filledcategories)<15:
        for player in range(nplayers):
            print(f'\n {playernames[player]}s TURN')
            cast0 = diceroll([])
            throws = 0
            while throws < 2:
        
                print(f"Current roll: {cast0}")
        
                
                selection = input("Which dice do you want to reroll? (Enter positions separated by spaces, or 'n' for no rerolls): ")
                while selection != n or
                if selection.lower() == 'n':
                    print("No rerolls selected.")
                    posibilities(cast0)
                    break

                # Get the indices for dice to reroll
                #TODO add error handling for user input

                replace_indices = list(map(int, selection.split()))
                for i in replace_indices:
                    cast0[i - 1] = 9  # Mark dice to reroll with 9

                # Reroll the selected dice
                cast0 = diceroll(cast0)
                throws += 1
                print(f"Your cast: {cast0}")
                posibilities(cast0)
            #print(displayscoreboard(filledcategories))
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
                    playerscore[player][category]=score
                    totalscore[player]+=score
                    print(f'category:{category} ,score:{score}')
                    print(displayscoreboard(filledcategories))
                    break
                else:
                    print('Either all categories are filled or invalid category.')
        print(displayscoreboard(filledcategories))
        print(f'Your current total score is:{totalscore}')    
    for player in range(nplayers):
        bonus=bonuscheck(playerscore[player])
        totalscore[player]+=bonus
        print(f'{playernames[player]} receives {bonus} points as bonus')
    #DEBUG for player in range(nplayers):
     #DEBUG   highscorevalue,highscorename=highscore(totalscore[player],playernames[player]),
    
    print('\n FINAL SCORES:')
    for player in range(nplayers):
        print(f'player{player}:{totalscore[player]}')
    

menu()

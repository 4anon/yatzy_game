from dice import *
from posibility_count import *
from scoreboard import *
from scoring import *


def categorychoice(filledcategories,cast):
    categories=[ "ones", "twos", "threes", "fours", "fives", "sixes",
        "one pair", "two pairs", "three of a kind", "four of a kind",
        'five of a kind',"small straight", "large straight",'fullstraight','villa','tower',"full house", "chance", "yatzy"]
    
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
    filledcategories_all={}
    for member in range(nplayers):
        player=input(f'Enter a name for player {player}: ')
        playernames.append(player)
        playerscore[player]={}
        totalscore[player]=0
        filledcategories_all[player]={}
    global highscorename,highscorevalue
    highscorename,highscorevalue=highscoreinstall()
    if highscorename='':
        print('no available highscore')
    else:
        print(f'the current highscore is {highscorename}:{highscorevalue}')
    while any(len(filledcategories_all[player])<15 for player in playernames):
        for player in playernames:
          if len(filledcategories_all[player])<15:
            print(f'\n {player}s TURN')
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
           
            while True:
                result=categorychoice(filledcategories_all[player],cast0)
                if result[0]:
                    print(result[0])
                else:
                    filledcategories_all[player]=result[1]
             
                if filledcategories_all[player]:
                  for category in filledcategories_all[player]:
                    score=filledcategories[player][category]
                    playerscore[player][category]=score
                    totalscore[player]+=score
                    print(f'category:{category} ,score:{score}')
                    print(displayscoreboard(filledcategories_all[player]))
                    break
                else:
                    print('Either all categories are filled or invalid category.')
        print(displayscoreboard(filledcategories_all[player]))
        print(f'Your current total score is:{totalscore[player]}')    
    for player in playernames:
        bonus=bonuscheck(playerscore[player])
        totalscore[player]+=bonus
        print(f'{player} receives {bonus} points as bonus')
    for player in playernames:
        highscorevalue,highscorename=highscore(totalscore[player],playernames[player])
    if highscorename:
        uploadhigscore(highscorename,highscorevalue) 
    print('\n FINAL SCORES:')
    for player in playernames:
        print(f'player{player}:{totalscore[player]}')
    

menu()
        print(f'player{player}:{totalscore[player]}')
    

menu()

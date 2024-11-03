from maxiposibility import *
from maxiboard import *
from maxiscoring import *

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
    gamefinished=0
    while gamefinished==0:
        gamefinished==1
        for player in playernames:
            if len(filledcategories_all[player])<21:
                gamefinished=1
                print(f'{player}s TURN')
                cast0=diceroll([])
                throws=0
                while throws<2:
                    print(f'Current roll:{cast0}')
                    selection=input("Which dice do you want to reroll? (Enter positions separated by spaces, or 'n' for no rerolls): ")
                    if selection.lower()=='n':
                        print('No rerolls selected')
                        posibilities(cast0)
                        break
                    try:
                        replaceindices=list(map(int,selection.split()))
                        if all(1<=i<=len(cast0)) for i in replaceindices):
                            for i in replaceindices:
                                cast0[i-1]=9
                        else:
                            print('Invalid dice positions.You may try again')
                            continue
                    except ValueError:
                        print('Invalid input.Either enter numbers seperated by spaces or enter n')
                        continue
                    cast0=diceroll(cast0)
                    throws+=1
                    print(f'Your cast:{cast0}')
                    posibilities(cast0)
                    print('\n'+ displayscoreboard(filledcategories_all[player],cast0))

                    while True:
                        result,updatedcategories=categorychoice(filledcategories_all[player],cast0)
                        print(result)
                        if result[0]:
                            print(result[0])
                        if updatedcategories!=filledcategories_all[player]:
                            filledcategories_all[player]=updatedcategories
                            for category in filledcategories_all[player]:
                                score=filledcategories_all[player][category]
                                playerscore[player][category]=score
                                totalscore[player]+=score
                                print(f'Category:{},Score:{score}')
                            print(displayscoreboard(filledcategories_all[player]))
                            break
                        else:
                            print('Either all categories are filled or invalid category.Try again')
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









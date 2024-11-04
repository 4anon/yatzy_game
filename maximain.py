from maxiposibility import *
from maxiboard import *
from maxiscoring import *

def menu():

    filledcategories = {}
    totalscore = {}
    playerscore = {}
    playernames = []
    filledcategories_all = {}


    #Error handling for player count
    while True:
        try:
            nplayers = int(input('Enter the number of players: '))
            if nplayers <= 0:
                print("Please enter a positive number of players.")
                continue
            break  # Exit loop if valid
        except ValueError:
            print("Invalid input. Please enter a number.")

    

    for member in range(nplayers):
        while True:
            player = input(f'Enter a name for player {member + 1}: ').strip()
            if not player:
                print("Player name cannot be empty. Please enter a valid name.")
            elif player in playernames:
                print(f"Name '{player}' is already taken. Please choose a different name.")
            else:
                playernames.append(player)  # Only add once, inside the validation loop
                break  # Exit loop if valid

        playerscore[player] = {}
        totalscore[player] = 0
        filledcategories_all[player] = {}


    global highscorename,highscorevalue
    highscorename,highscorevalue = highscoreinstall()

    if highscorename == '':
        print('no available highscore')
    else:
        print(f'the current highscore is {highscorename}:{highscorevalue}')

    gamefinished = 0
    try:
        while gamefinished == 0:
            gamefinished = 1  # Assume game is finished unless proven otherwise
            for player in playernames:
                if len(filledcategories_all[player]) < 21:  # Check if player has categories left to fill
                    gamefinished = 0  # Set gamefinished to 0 if at least one player has categories left
                    print(f'{player}\'s TURN')
                    cast0 = diceroll([])
                    throws = 0
                    while throws < 2:
                        print(f'Current roll: {cast0}')
                        selection = input("Which dice do you want to reroll? (Enter positions separated by spaces, or 'n' for no rerolls): ")
                        if selection.lower() == 'n':
                            print('No rerolls selected')
                            posibilities(cast0)
                            break  # Proceed directly to category choice if "n" is selected

                        try:
                            replaceindices = list(map(int, selection.split()))
                            if all(1 <= i <= len(cast0) for i in replaceindices):
                                for i in replaceindices:
                                    cast0[i - 1] = 9  # Mark dice for reroll
                            else:
                                print('Invalid dice positions. Try again.')
                                continue  
                        except ValueError:
                            print('Invalid input. Please enter numbers separated by spaces, or enter "n" to skip.')
                            continue

                        # Perform the reroll
                        cast0 = diceroll(cast0)
                        throws += 1
                        print(f'Your new roll: {cast0}')
                        posibilities(cast0)

                        if throws < 2:
                            reroll_prompt = input("Would you like to reroll again? (y/n): ")
                            if reroll_prompt.lower() == 'n':
                                break  # Break here to go to category choice if "n" is chosen

                    print('\nProceeding to category choice...')
                    
                    category_chosen = False  # Added
                    
                    while not category_chosen:  # Added instead of while true
                        result, updated_categories = categorychoice(filledcategories_all[player], cast0)
                        print(result)
                        if "scored" in result:  # Success message implies category was added
                            for category in updated_categories:
                                score = updated_categories[category]
                                playerscore[player][category] = score
                                totalscore[player] += score
                                print(f'Category: {category}, Score: {score}')
                            category_chosen = True
                            break 
                        else:
                            print('Either all categories are filled or invalid category. Try again.')
                    print(f'\n{player.capitalize()}:')
                    print(displayscoreboard(filledcategories_all[player]))
                    print(f'Your current total score is: {totalscore[player]}')

    except Exception as e:
        print(f"An unexpected error occurred: {e}. Please try again.")



    # Final score and high score display
    for player in playernames:
        bonus = bonuscheck(playerscore[player])
        totalscore[player] += bonus
        print(f'{player} receives {bonus} points as bonus')
    for player in playernames:
        highscorevalue, highscorename = highscore(totalscore[player], player)
    if highscorename:
        uploadhighscore(highscorename, highscorevalue) 
        print('\n FINAL SCORES:')
    for player in playernames:
        print(f'player{player}:{totalscore[player]}')

menu()

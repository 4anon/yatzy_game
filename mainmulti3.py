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
    playerscore = {}
    totalscore = {}
    playernames = []
    filledcategories_all_players = {}

    for player in range(nplayers):
        name = input(f'Enter a name for player {player + 1}: ')
        playernames.append(name)
        playerscore[player] = {}
        totalscore[player] = 0
        filledcategories_all_players[player] = {}

    global highscorename, highscorevalue
    highscorename, highscorevalue = highscoreinstall()

    if highscorename is None:
        print("No high score available.")
    else:
        print(f"Current high score is {highscorevalue} by {highscorename}")

    # Loop until each player has filled all categories
    while True:
        all_categories_filled = True  # Initialize the flag as True
        for player in range(nplayers):
            # Check if the player has filled all categories
            if len(filledcategories_all_players[player]) < 15:
                all_categories_filled = False  # Set flag to False if any player has remaining categories
                break

        if all_categories_filled:
            break  # Exit the loop if all players have filled all categories

        for player in range(nplayers):
            if len(filledcategories_all_players[player]) == 15:
                continue  # Skip turn if player has filled all categories

            print(f"\n{playernames[player]}'s TURN")
            cast0 = diceroll([])
            throws = 0
            while throws < 2:
                print(f"Current roll: {cast0}")
                selection = input("Which dice do you want to reroll? (Enter positions separated by spaces, or 'n' for no rerolls): ")

                if selection.lower() == 'n':
                    print("No rerolls selected.")
                    posibilities(cast0)
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

            # Show the player's current scoreboard before choosing a category
            print("\n" + displayscoreboard(filledcategories_all_players[player]))

            # Choose category and update the individual scoreboard
            while True:
                result = categorychoice(filledcategories_all_players[player], cast0)
                if result[0]:
                    print(result[0])
                else:
                    filledcategories_all_players[player] = result[1]

                # Update the player’s score and break the loop if successful
                if filledcategories_all_players[player]:
                    for placement in filledcategories_all_players[player]:
                        category = placement
                    score = filledcategories_all_players[player][category]
                    playerscore[player][category] = score
                    totalscore[player] += score
                    print(f"Category: {category}, Score: {score}")
                    break
                else:
                    print("Either all categories are filled or invalid category.")

            # Show updated scoreboard for the current player
            print("\n" + displayscoreboard(filledcategories_all_players[player]))
            print(f"Current Total Score for {playernames[player]}: {totalscore[player]}")

    # Add bonus if applicable, display final scores, and check high scores
    for player in range(nplayers):
        bonus = bonuscheck(playerscore[player])
        totalscore[player] += bonus
        print(f"{playernames[player]} receives {bonus} points as bonus")

    for player in range(nplayers):
        highscorevalue, highscorename = highscore(totalscore[player], playernames[player])

    print("\nFINAL SCORES:")
    for player in range(nplayers):
        print(f"{playernames[player]}: {totalscore[player]}")

# Run the game
menu()
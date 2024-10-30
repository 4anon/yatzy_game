from dice import *
from posibility_count import *
import random
from scoreboard import *
from scoring import *

def categorychoice(filledcategories, cast):
    categories = ["ones", "twos", "threes", "fours", "fives", "sixes",
                  "one pair", "two pairs", "three of a kind", "four of a kind",
                  "small straight", "large straight", "full house", "chance", "yatzy"]

    category = input('Enter a category: ').strip().lower()
    if category in filledcategories:
        return 'This category is filled. Choose a different one.'
    if category not in categories:
        return 'Invalid category. Try again.'

    score = scorecalculation(category, cast)
    filledcategories[category] = score

    return f'You scored {score} points in the {category}', filledcategories

def menu():
    scoredcategories = {}
    filledcategories = {}
    totalscore = 0

    while len(filledcategories) < 15:
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

        print(displayscoreboard(filledcategories))

        # Call categorychoice function
        result = categorychoice(filledcategories, cast0)

        # Check if result is a string (error message) without isinstance
        if type(result) == str:
            print(result)  # Print the message if the category is filled or invalid
            continue  # Skip the rest of this loop and ask for input again

        # Otherwise, update filledcategories with the dictionary from result
        filledcategories = result[1]

        # Get the last added category to calculate score
        last_category = list(filledcategories.keys())[-1]
        score = int(filledcategories[last_category])
        totalscore += score
        print(f'Category: {last_category}, Score: {score}')

        print(displayscoreboard(filledcategories))
        print(f'Your current total score is: {totalscore}')

    print(f'Your final total score is: {totalscore}')

menu()

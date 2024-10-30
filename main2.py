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

    # Calculate the score for the chosen category
    score = scorecalculation(category, cast)
    print(f"Debug: Calculated score for {category} is {score}")  # Debugging output

    # Attempt to convert score to an integer, handle invalid score
    try:
        score = int(score)
    except (TypeError, ValueError):
        return 'Error calculating score. Please try a different category.'

    # Update filledcategories with the calculated score
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

            # Get valid dice positions for reroll
            replace_indices = []
            for i in selection.split():
                if i.isdigit() and 1 <= int(i) <= len(cast0):
                    replace_indices.append(int(i) - 1)  # Adjust for zero-based indexing
                else:
                    print(f"Ignoring invalid position: {i}")

            # Reroll the selected dice
            for i in replace_indices:
                cast0[i] = 9  # Mark dice to reroll with 9

            cast0 = diceroll(cast0)
            throws += 1
            print(f"Your cast: {cast0}")
            posibilities(cast0)

        print(displayscoreboard(filledcategories))

        # Now ask for the category choice after rerolls are finalized
        result = categorychoice(filledcategories, cast0)

        # Check if result is an error message
        if isinstance(result, str):
            print(result)  # Print error message if the category is filled or invalid
            continue  # Go back to reroll phase

        # Otherwise, update filledcategories with the score
        filledcategories = result[1]

        # Get the last added category and its score
        last_category = list(filledcategories.keys())[-1]
        score = int(filledcategories[last_category])
        totalscore += score
        print(f'Category: {last_category}, Score: {score}')

        print(displayscoreboard(filledcategories))
        print(f'Your current total score is: {totalscore}')

    print(f'Your final total score is: {totalscore}')

menu()

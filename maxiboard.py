import random
from scoring import *

def displayscoreboard(scoredcategories):
    categories=[ "ones", "twos", "threes", "fours", "fives", "sixes",
        "one pair", "two pairs", "three of a kind", "four of a kind",
        'five of a kind',"small straight", "large straight",'fullstraight','villa','tower',"full house", "chance", "yatzy"]
    lines=['\nSCOREBOARD']
    for category in categories:
       if category in scoredcategories:
          score=scoredcategories[category]
          lines.append(f'{category}:{score}')
       else:
          lines.append(f'{category}:     ')
    lines.append('')
    output='\n'.join(lines)
    return output

def scorecalculation(choice, cast):
    choice = choice.replace(" ", "")  # Remove spaces for consistent matching

    if choice == 'ones':
        return scorenumber(cast, 1)
    elif choice == 'twos':
        return scorenumber(cast, 2)
    elif choice == 'threes':
        return scorenumber(cast, 3)
    elif choice == 'fours':
        return scorenumber(cast, 4)
    elif choice == 'fives':
        return scorenumber(cast, 5)
    elif choice == 'sixes':
        return scorenumber(cast, 6)
    elif choice == 'onepair':
        return onepair(cast)
    elif choice == 'twopairs':
        return twopair(cast)
    elif choice == 'threeofakind':
        return threekind(cast)
    elif choice == 'fourofakind':
        return fourkind(cast)
    elif choice=='fiveofkind':
        return fiveofakind(cast)
    elif choice == 'smallstraight':
        return smallstraight(cast)
    elif choice == 'largestraight':
        return largestraight(cast)
    elif choice=='fullstraight':
        return fullstraight(cast)
    elif choice == 'fullhouse':
        return fullhouse(cast)
    elif choice=='villa':
        return villa(cast)
    elif choice=='tower':
        return tower(cast)
    elif choice == 'chance':
        return sum(cast)
    elif choice == 'yatzy':
        return yatzycheck(cast)
    else:
        return None  # Return None for invalid category

def categorychoice(filledcategories, cast):
    categories = [
        "ones", "twos", "threes", "fours", "fives", "sixes",
        "one pair", "two pairs", "three of a kind", "four of a kind",
        'five of a kind', "small straight", "large straight", 'fullstraight',
        'villa', 'tower', "full house", "chance", "yatzy"
    ]
    
    category = input('Enter a category: ').strip().lower()
    print(f"Debug: Current filled categories are {filledcategories}")  # Debug 

    if category in filledcategories:
        return 'This category is filled, choose a different one', filledcategories  # Return a tuple
    if category not in categories:
        return 'Invalid category, try again', filledcategories  # Return a tuple

    try:
        score = scorecalculation(category, cast)
        filledcategories[category] = int(score)  # Update filled categories with the score
        return f'You scored {score} points in the {category}', filledcategories  # Return success message and updated categories
    except (ValueError, TypeError):
        return 'Type error or value error, try again', filledcategories  # Return a tuple

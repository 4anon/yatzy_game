import random
from scoring import *

def displayscoreboard(scoredcategories):
    lines = ['\nSCOREBOARD']
    for category,score in scoredcategories.items():
        lines.append(f'{category}:{score}')
    lines.append('')
    output='\n'.join(lines)
    return output

def scorecalculation(choice,cast):
    if choice=='ones':
        return scorenumber(cast,1)
    elif choice=='twos':
        return scorenumber(cast,2)
    elif choice=='threes':
        return scorenumber(cast,3)
    elif choice=='fours':
        return scorenumber(cast,4)
    elif choice=='fives':
        return scorenumber(cast,5)
    elif choice=='sixes':
        return scorenumber(cast,6)
    elif choice=='onepair':
        return onepair(cast)
    elif choice=='twoppair':
        return twopair(cast)
    elif choice=='threeofakind':
        return threekind(cast)
    elif choice=='fourofakind':
        return fourkind(cast)
    elif choice=='smallstraight':
        return smallstraight(cast)
    elif choice=='largestraight':
        return largestraight(cast)
    elif choice=='fullhouse':
        return fullhouse(cast)
    elif choice=='chance':
        return sum(cast)
    elif choice=='yatzy':
        return yatzycheck(cast)
    else:
        return 'invalid category'
    
def categorychoice(pssibility,filledcategories,cast):
    category=input('entera category').strip().lower()
    if category in filledcategory:
        return 'this category is filled choose a different one'
    if category not in possibility:
        return 'invalid category try again'
    score=scorecalculation(cast,category)
    filledcategories[category]=score
    return f'You scored {score} points in the {category}',filledcategories


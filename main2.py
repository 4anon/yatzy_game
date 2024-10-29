def categorychoice(filledcategories,cast):
    categories=[ "ones", "twos", "threes", "fours", "fives", "sixes",
        "onepair", "twopairs", "threeofakind", "fourofakind",
        "smallstraight", "largestraight", "fullhouse", "chance", "yatzy"]
    
    category=input('enter a category').strip().lower()
    if category in filledcategories:
        return 'this category is filled choose a different one'
    if category not in categories:
        return 'invalid category try again'
    filledcategories[category]=score
    return f'You scored {score} points in the {category}',filledcategories

def menu():
 scoredcategories={}
 filledcategories={}
 totalscore=0
 
 while len(filledcategories)<15:
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
    filledcategories=categorychoice(filledcategories,cast0)
    if filledcategories:
        for placement in filledcategories:
            category=placement
        score=filledcategories[category]
        totalscore+=score
        print(f'category:{category} ,score:{score}')
    print(displayscoreboard(filledcategories))
    print(f'Your current total score is:{totalscore}')
 print(f'Your final total score is:{totalscore}')
            
    

menu()

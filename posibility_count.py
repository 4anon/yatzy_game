from collections import Counter
import random

def posibilities(cast):
    posibility = {
        "ones": 0, "twos": 0, "threes": 0, "fours": 0, "fives": 0, "sixes": 0,
        "one pair": 0, "two pairs": 0, "three of a kind": 0, "four of a kind": 0,
        "small straight": 0, "large straight": 0, "full house": 0, "chance":0, "yatzy": 0
    }

    # Count occurrences of each number
    counts = Counter(cast)

    # Assign values to possibilities based on counts
    for number, count in counts.items():
        if number == 1:
            posibility["ones"] += count
        elif number == 2:
            posibility["twos"] += count * 2
        elif number == 3:
            posibility["threes"] += count * 3
        elif number == 4:
            posibility["fours"] += count * 4
        elif number == 5:
            posibility["fives"] += count * 5
        elif number == 6:
            posibility["sixes"] += count * 6
    
    #one pair
    highest_pair = 0
    for num, count in counts.items():
        if count >= 2:
            pair_value = num * 2
            if pair_value > highest_pair:
                highest_pair = pair_value

    posibility["one pair"] = highest_pair

    two_pair_values = []
    for num, count in counts.items():
        if count >= 2:
            two_pair_values.append(num)

    if len(two_pair_values) >= 2:
        posibility["two pairs"] = (two_pair_values[0] + two_pair_values[1]) * 2
        
    # Check for three of a kind
    for num, count in counts.items():
        if count >= 3:
            posibility["three of a kind"] = num * 3
            break  # Stop after finding the first three of a kind
            
    # four of a kind  
    for num, count in counts.items():
        if count >= 4:
            posibility["four of a kind"] = num * 4
            break  # Stop after finding the first three of a kind
            
    # Check for small straight (1, 2, 3, 4, 5)
    if set([1, 2, 3, 4, 5]).issubset(cast):
        posibility["small straight"] = 15

    # Check for small straight (1, 2, 3, 4, 5)
    if set([2, 3, 4, 5 ,6]).issubset(cast):
        posibility["large straight"] = 20
        
    # full house
    if sorted(counts.values()) == [2, 3]:  # Full house condition
        posibility["full house"] = sum(cast) 
        
    #chans
    posibility["chance"] = sum(cast)

    # Check for yatzy (all five dice are the same)
    if len(counts) == 1:  # All numbers are the same
        posibility["yatzy"] = 50
    
    # Display non-zero possibilities
    for key, value in posibility.items():
        if value != 0:
            print(f"{key} : Your Value: {value}")



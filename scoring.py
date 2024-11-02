import random

def diceroll(reroll):
    rolls=[]
    if not reroll:
      for i in range(5):
       roll=random.randint(1,6)
       rolls.append(roll)
    elif reroll:
       for i in range(len(reroll)):
          if reroll[i]==9:
             reroll[i]=random.randint(1,6)
       rolls=reroll
    return rolls

def totalscore(dice):
    return sum(dice)

def yatzycheck(dice):
    score=0
    if dice.count(dice[0])==5:
        score=50
    return score

def scorenumber(dice,number):
    count=dice.count(number)
    score=count*number
    return score
def scorepair(dice):
    pairs=[]
    for die in set(dice):
        if dice.count(die)>=2:
            pairs.append(die)
    score=0
    highestpair=0
    if len(pairs)>0:
        highestpair=max(pairs)
    else:
        highestpair=0
    score=highestpair*2
    return score

def onepair(dice):
    for die in set(dice):
        if dice.count(die)>=2:
            score=die*2
            return score
    return 0
def twopair(dice):
    pairs=[]
    for die in set(dice):
        if dice.count(die)>=2:
            pairs.append(die)
    if len(pairs)>=2:
        score=(pairs[0]*2)+(pairs[1]*2)
        return score
    return 0

def threekind(dice):
    for die in set(dice):
        if dice.count(die)>=3:
            score=die*3
            return score
    return 0

def fourkind(dice):
    for die in set(dice):
        if dice.count(die)>=4:
            score=die*4
            return score
    return 0
def smallstraight(dice):
    sorteddice=sorted(set(dice))
    if sorteddice==[1,2,3,4,5]:
        return 15
    return 0

def largestraight(dice):
    sorteddice=sorted(set(dice))
    if sorteddice==[2,3,4,5,6]:
        return 20
    return 0
def fullhouse(dice):
    unidice=set(dice)
    if len(unidice)==2:
        countone=dice.count(unidice[0])
        countsecond=dice.count(unidice[1])
        if (countone==3 and countsecond==2) or (countone==2 and countsecond==3):
            score=unidice[0]*countone+unidice[1]*countsecond
            return score
    return 0
            
def bonuscheck(scorecategories):
    uppersection=['ones','twos','threes','fours','fives','sixes']
    upperscore=0
    for category in uppersection:
        if category in scoredcategories:
            upperscore+=scoredcategories[category]
        if upperscore>=63:
            return 50
    return 0

def highscore(totalscore,playername):
    global highscore,highscorename
    if totalscore>highscore:
        highscore=totalscore
        highscorename=playername
    return highscore,highscorename
    
def highscoreinstall():
    try: 
        with open('highscore.txt','r') as file:
            score = file.read().strip().split(',')
            if len(score) == 2:
                highscorename = score[0]
                highscore = int(score[1])
                return highscorename, highscore
            else:
                return '',0  # Fallback if the file doesn’t contain two elements
    except (ValueError, FileNotFoundError):  # Handle both missing file and value errors
        return '',0  # Default return value if there's an error

def uploadhighscore(highscorename, highscore):
    with open('highscore.txt', 'w') as file:
        file.write(f'{highscorename},{str(highscore)}')  # Use ',' to match the expected format

